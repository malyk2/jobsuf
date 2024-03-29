<template>
  <div class="w-full lg:w-12/12 px-4">
    <card-base>
      <template v-slot:header>
        <h6 class="text-blueGray-700 text-xl font-bold">Jobs</h6>
      </template>
      <div class="w-full flex flex-wrap">
        <div class="w-full lg:w-2/12 px-4">
          <select-base label="RSS" firstOption="RSS" v-model="filter.rss_id" size="small" :options="rsss"
            optionsType="objects" @change="runFilter" />
        </div>
        <div class="w-full lg:w-2/12 px-4">
          <select-base label="Country" firstOption="Country" v-model="filter.country_id" size="small"
            :options="countries" optionsType="objects" optionTitleType="name" @change="runFilter" />
        </div>
        <div class="w-full lg:w-2/12 px-4">
          <select-base label="Period" firstOption="Period" v-model="filter.period" size="small" :slotOptions="true"
            @change="runFilter">
            <option value="">Period</option>
            <option value="last_week">Last week</option>
            <option value="last_2_weeks">Last 2 weeks</option>
            <option value="last_month">Last month</option>
            <option value="last_2_months">Last 2 months</option>
          </select-base>
        </div>
        <div class="w-full lg:w-1/12 px-4">
          <checkbox-base label="Unread" v-model="filter.only_unread" @change="runFilter" />
        </div>
        <div class="w-full lg:w-3/12 px-4 flex">
          <div class="w-1/3">
            <checkbox-base label="Favorited" v-model="filter.only_favourited" @change="filterFavourited" />
          </div>
          <div class="w-2/3">
            <select-base v-show="filter.only_favourited" label="Rate" firstOption="Rate"
              v-model="filter.favourited_rate" size="small" :options="[1, 2, 3, 4, 5]" @change="runFilter" />
          </div>
        </div>
        <div class="w-full lg:w-2/12 p-4 flex items-center justify-center">
          <div class="w-1/2">
            <button-base color="danger" size="small" title="Reset" @click="resetFilter()">
              Reset
            </button-base>
          </div>
          <div class="w-1/2">
            <button-base color="info" size="small" title="Advanced" @click="showAdwansedFilter = !showAdwansedFilter">
              <i :class="
                showAdwansedFilter
                  ? 'fa fa-arrow-circle-up'
                  : 'fa fa-arrow-circle-down'
              "></i>
            </button-base>
          </div>
        </div>
        <template v-if="showAdwansedFilter">
          <!-- <div -->
          <div class="flex w-full lg:w-6/12 rounded-md border border-gray-100">
            <div class="w-full lg:w-2/4 px-1">
              <select-base label="Price" size="small" v-model="priceFilter.type" optionsType="objects"
                optionValueType="value" :options="[
                  { title: 'Budget', value: 'budget' },
                  { title: 'Hourly from', value: 'rate_from' },
                  { title: 'Hourly to', value: 'rate_to' },
                  { title: 'No rate', value: 'no_rate' },
                ]" />
            </div>
            <div class="w-full lg:w-1/4 px-1" v-if="this.priceFilter.type !== 'no_rate'">
              <select-base label="Operator" size="small" v-model="priceFilter.operator" optionsType="objects"
                optionValueType="value" :options="[
                  { title: '>=', value: 'gte' },
                  { title: '<=', value: 'lte' },
                ]" />
            </div>
            <div class="w-full lg:w-1/4 px-1" v-if="this.priceFilter.type !== 'no_rate'">
              <input-base label="Value" size="small" v-model="priceFilter.value" />
            </div>
          </div>
          <div class="flex w-full lg:w-6/12 rounded-md border border-gray-100">
            <div class="w-full lg:w-1/4 px-1">
              <select-base label="Date" size="small" v-model="dateFilter.field" optionsType="objects"
                optionValueType="value" :options="[
                  { title: 'Created', value: 'created' },
                  { title: 'Published', value: 'published' },
                ]" />
            </div>
            <div class="w-full lg:w-1/4 px-1">
              <select-base label="Operator" size="small" v-model="dateFilter.operator" optionsType="objects"
                optionValueType="value" :options="[
                  { title: '>=', value: 'gte' },
                  { title: '<=', value: 'lte' },
                  { title: '=', value: '' },
                ]" />
            </div>
            <div class="w-full lg:w-2/4 px-1">
              <input-base label="Value" size="small" v-model="dateFilter.value" type="date" />
            </div>
          </div>
          <div class="flex w-full lg:w-6/12">
            <div class="w-full lg:w-1/2">
              <input-base label="Search" size="small" v-model="filter.search" />
            </div>
            <div class="w-full lg:w-1/2 flex items-center justify-center">
              <button-base color="success" size="small" title="Filter" @click="runFilter()" class="mt-3">
                Run
              </button-base>
            </div>
          </div>
          <div class="flex w-full lg:w-6/12">
            <div class="w-full lg:w-1/2 flex items-center justify-center">
            </div>
          </div>
        </template>
      </div>
      <div class="block w-full overflow-x-auto">
        <div class="flex justify-center">
          <paginator-admin :paginator="paginator" @paginate="getItems" :showOnePage="true" />
        </div>
        <table class="items-center w-full bg-transparent border-collapse">
          <tbody>
            <template v-for="item in items" :key="item.id">
              <tr :class="{ 'text-blueGray-400': item.is_readed_by_auth_user }">
                <table-td class="w-9/12">
                  {{ item.title }}
                  <a :href="item.upwork_id" target="_blank" rel="noopener noreferrer">
                    <i class="fas fa-link text-sm"></i>
                  </a>
                  <div class="float-right">
                    <button-base color="info" size="mini" title="Show detail" @click="toggleShowDetail(item.id)">
                      <i :class="
                        isShowedDetail(item.id)
                          ? 'fa fa-arrow-circle-up'
                          : 'fa fa-arrow-circle-down'
                      "></i>
                    </button-base>
                    <button-base :color="
                      item.is_readed_by_auth_user ? 'danger' : 'warning'
                    " size="mini" :title="
  item.is_readed_by_auth_user
    ? 'Mark as unread'
    : 'Mark as read'
" @click="markRead([item.id], !item.is_readed_by_auth_user)">
                      <i :class="
                        item.is_readed_by_auth_user
                          ? 'fas fa-eye-slash'
                          : 'fas fa-eye'
                      "></i>
                    </button-base>
                    <button-base :color="item.is_favourited ? 'success' : 'warning'" size="mini" :title="
                      item.is_favourited
                        ? 'Mark as unfavourite'
                        : 'Mark as favourite'
                    " @click="toogleRate(item)">
                      <i class="fas fa-heart"></i>
                    </button-base>
                    <rates class="mt-1" v-if="item.is_favourited" :rate="item.favourited_rate" :defaultRate="0"
                      @change="(rate) => markFavourite(item, rate, true)" />
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
              <tr v-show="isShowedDetail(item.id)" :class="{ 'text-blueGray-400': item.is_readed_by_auth_user }">
                <table-td v-html="item.content" colspan="3"> </table-td>
              </tr>
            </template>
          </tbody>
        </table>
        <div class="flex justify-center">
          <paginator-admin :paginator="paginator" @paginate="getItems" :showOnePage="true" />
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
import InputBase from "@/components/Inputs/InputBase.vue";
import CheckboxBase from "@/components/Inputs/CheckboxBase.vue";
import Paginator from "@/libs/Paginator";
import Rates from "@/components/Rates/Rates.vue";
import { rssUpwork as api } from "@/api";

export default {
  data() {
    return {
      color: "light",
      items: [],
      paginator: new Paginator(
        this.$route.query.limit || 15,
        this.$route.query.offset || 0
      ),
      showedIds: [],
      filter: {
        rss_id: this.$route.query.rss_id || null,
        country_id: this.$route.query.country_id || null,
        only_unread: this.$route.query.only_unread == "true" ? true : false,
        only_favourited:
          this.$route.query.only_favourited == "true" ? true : false,
        favourited_rate: this.$route.query.favourited_rate || null,
        search: this.$route.query.search || null,
        period: this.$route.query.period || 'last_week',
      },
      showAdwansedFilter: false,
      priceFilter: {
        type: "rate_to",
        operator: "gte",
        value: null,
      },
      dateFilter: {
        field: "created",
        operator: "gte",
        // value:  new Date().toISOString().split('T')[0],
        value: "",
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
    InputBase,
    Rates,
  },
  mounted() {
    this.getItems();
    this.getFilterOptions();
  },
  methods: {
    getItems() {
      let query = this.listQuery;
      api.jobsIndex(query).then((response) => {
        this.$router.replace({ query: query });
        this.items = response.results;
        this.paginator.createPaginator(response.count);
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
    runFilter() {
      this.paginator.setPage(1);
      this.getItems();
    },
    resetFilter() {
      this.paginator.setPage(1);
      for (const key in this.filter) {
        const element = this.filter[key];
        if (typeof element == "boolean") {
          this.filter[key] = false;
        } else if (typeof element == "string") {
          this.filter[key] = null;
        }
        this.priceFilter.value = "";
        this.dateFilter.value = "";
      }
      this.getItems();
    },
    filterFavourited() {
      this.paginator.setPage(1);
      if (!this.filter.only_favourited) {
        this.filter.favourited_rate = null;
      }
      this.getItems();
    },
  },
  computed: {
    listQuery() {
      let query = {
        offset: this.paginator.offset,
        limit: this.paginator.limit,
      };
      for (const key in this.filter) {
        const element = this.filter[key];
        if (element !== null && element !== "") {
          query[key] = element;
        }
      }
      if (this.priceFilter.type == "no_rate") {
        query["no_rate"] = true;
      } else if (this.priceFilter.value) {
        query[this.priceFilter.type + "__" + this.priceFilter.operator] =
          this.priceFilter.value;
      }
      if (this.dateFilter.value !== "") {
        const sufix =
          this.dateFilter.operator !== ""
            ? "__" + this.dateFilter.operator
            : "";
        query[this.dateFilter.field + sufix] = this.dateFilter.value;
      }
      return query;
    },
  },
};
</script>
