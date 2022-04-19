<template>
  <div class="w-full lg:w-12/12 px-4">
    <card-base>
      <template v-slot:header>
        <h6 class="text-blueGray-700 text-xl font-bold">Jobs</h6>
      </template>
      <div class="block w-full flex flex-wrap">
        <div class="w-full lg:w-3/12 px-4">
          <select-base
            label="RSS"
            firstOption="RSS"
            v-model="filter.rss_id"
            size="small"
            :options="rsss"
            optionsType="objects"
            @change="getItems"
          />
        </div>
        <div class="w-full lg:w-3/12 px-4">
          <select-base
            label="Country"
            firstOption="Country"
            v-model="filter.country_id"
            size="small"
            :options="countries"
            optionsType="objects"
            optionTitleType="name"
            @change="getItems"
          />
        </div>
        <div class="w-full lg:w-3/12 px-4">
          <checkbox-base
            label="Unread"
            v-model="filter.only_unread"
            @change="getItems"
          />
        </div>
        <div class="w-full lg:w-3/12 px-4 flex">
          <div class="w-1/3">
            <checkbox-base
              label="Favorited"
              v-model="filter.only_favourited"
              @change="filterFavourited"
            />
          </div>
          <div class="w-2/3">
            <select-base
              v-show="filter.only_favourited"
              label="Rate"
              firstOption="Rate"
              v-model="filter.favourited_rate"
              size="small"
              :options="[1, 2, 3, 4, 5]"
              @change="getItems"
            />
          </div>
        </div>
      </div>
      <div class="block w-full overflow-x-auto">
        <table class="items-center w-full bg-transparent border-collapse">
          <tbody>
            <template v-for="item in items" :key="item.id">
              <tr :class="{ 'text-blueGray-400': item.is_readed_by_auth_user }">
                <table-td class="w-9/12">
                  {{ item.title }}
                  <a
                    :href="item.upwork_id"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <i class="fas fa-link text-sm"></i>
                  </a>
                  <div class="float-right">
                    <button-base
                      color="info"
                      size="mini"
                      title="Show detail"
                      @click="toggleShowDetail(item.id)"
                    >
                      <i
                        :class="
                          isShowedDetail(item.id)
                            ? 'fa fa-arrow-circle-up'
                            : 'fa fa-arrow-circle-down'
                        "
                      ></i>
                    </button-base>
                    <button-base
                      :color="
                        item.is_readed_by_auth_user ? 'danger' : 'warning'
                      "
                      size="mini"
                      :title="
                        item.is_readed_by_auth_user
                          ? 'Mark as unread'
                          : 'Mark as read'
                      "
                      @click="markRead([item.id], !item.is_readed_by_auth_user)"
                    >
                      <i
                        :class="
                          item.is_readed_by_auth_user
                            ? 'fas fa-eye-slash'
                            : 'fas fa-eye'
                        "
                      ></i>
                    </button-base>
                    <!-- <button-base
                      :color="item.is_favourited ? 'success' : 'warning'"
                      size="mini"
                      :title="
                        item.is_favourited
                          ? 'Mark as unfavourite'
                          : 'Mark as favourite'
                      "
                      @click="markFavourite([item.id], !item.is_favourited)"
                    >
                      <i class="fas fa-heart"></i>
                    </button-base> -->
                    <button-base
                      :color="item.is_favourited ? 'success' : 'warning'"
                      size="mini"
                      :title="
                        item.is_favourited
                          ? 'Mark as unfavourite'
                          : 'Mark as favourite'
                      "
                      @click="toogleRate(item)"
                    >
                      <i class="fas fa-heart"></i>
                    </button-base>
                    <rates
                      class="mt-1"
                      v-if="item.is_favourited"
                      :rate="item.favourited_rate"
                      :defaultRate="0"
                      @change="(rate) => markFavourite(item, rate, true)"
                    />
                  </div>
                </table-td>
                <table-td>
                  <div>
                    {{
                      item.rate_from
                        ? "Rate: $" + item.rate_from + "-$" + item.rate_to
                        : item.budget
                        ? "Budget: " + item.budget
                        : "No rate"
                    }}
                  </div>
                  <div>
                    {{ item.rss }}
                  </div>
                  <div>
                    {{ item.country }}
                  </div>
                </table-td>
                <table-td> {{ item.created }} </table-td>
              </tr>
              <tr
                v-show="isShowedDetail(item.id)"
                :class="{ 'text-blueGray-400': item.is_readed_by_auth_user }"
              >
                <table-td v-html="item.content" colspan="3"> </table-td>
              </tr>
            </template>
          </tbody>
        </table>
        <div class="flex justify-center">
          <paginator-admin :paginator="paginator" @paginate="getItems" />
        </div>
      </div>
    </card-base>
  </div>
</template>
<script>
import CardBase from "@/components/Cards/CardBase.vue";
import ButtonBase from "@/components/Buttons/ButtonBase.vue";
import TableTd from "@/components/Table/TableTd.vue";
import PaginatorAdmin from "@/components/Paginators/PaginatorAdmin.vue";
import SelectBase from "@/components/Inputs/SelectBase.vue";
import CheckboxBase from "@/components/Inputs/CheckboxBase.vue";
import Paginator from "@/libs/Paginator";
import Rates from "@/components/Rates/Rates.vue";
import { rssUpwork as api } from "@/api";

export default {
  data() {
    return {
      color: "light",
      items: [],
      paginator: new Paginator(15),
      showedIds: [],
      filter: {
        rss_id: null,
        country_id: null,
        only_unread: false,
        only_favourited: false,
        favourited_rate: null,
      },
      rsss: [],
      countries: [],
    };
  },
  components: {
    CardBase,
    ButtonBase,
    TableTd,
    PaginatorAdmin,
    SelectBase,
    CheckboxBase,
    Rates,
  },
  mounted() {
    this.getItems();
    this.getFilterOptions();
  },
  methods: {
    getItems() {
      api.jobsIndex(this.listQuery).then((response) => {
        this.items = response.results;
        this.paginator.setCount(response.count);
      });
    },
    getFilterOptions() {
      api.jobsFilterOptions().then((response) => {
        this.rsss = response.rsss;
        this.countries = response.countries;
      });
    },
    markRead(ids, readed) {
      const data = ids.map((id) => ({ id: id, readed: readed }));
      api.jobsMarkRead(data).then(() => {
        ids.forEach((id) => {
          let item = this.items.find((item) => item.id == id);
          if (item) {
            item.is_readed_by_auth_user = readed;
          }
        });
      });
    },
    toogleRate(item) {
      if (item.is_favourited) {
        this.markFavourite(item, null, false);
      } else {
        item.is_favourited = true;
      }
    },
    markFavourite(item, rate, favourited) {
      const data = [{ id: item.id, rate: rate, favourited: favourited }];
      api.jobsMarkFavourite(data).then(() => {
        item.is_favourited = favourited;
        item.favourited_rate = rate;
      });
    },
    toggleShowDetail(id) {
      if (this.isShowedDetail(id)) {
        const index = this.showedIds.indexOf(id);
        if (index > -1) {
          this.showedIds.splice(index, 1);
        }
      } else {
        this.showedIds.push(id);
      }
    },
    isShowedDetail(id) {
      return this.showedIds.includes(id);
    },
    filterFavourited() {
      if (!this.filter.only_favourited) {
        this.filter.favourited_rate = null;
      }
      this.getItems();
    },
  },
  computed: {
    listQuery() {
      let filter = {
        offset: this.paginator.offset,
        limit: this.paginator.limit,
      };
      for (const key in this.filter) {
        const element = this.filter[key];
        if (element !== null && element !== "") {
          filter[key] = element;
        }
      }
      return filter;
    },
  },
};
</script>
