<template>
  <div class="w-full lg:w-12/12 px-4">
    <card-base>
      <template v-slot:header>
        <h6 class="text-blueGray-700 text-xl font-bold">Jobs</h6>
      </template>
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
                    <button-base
                      :color="item.is_favourited ? 'success' : 'warning'"
                      size="mini"
                      :title="
                        item.is_favourited
                          ? 'Mark as favourite'
                          : 'Mark as unfavourite'
                      "
                      @click="markFavourite([item.id], !item.is_favourited)"
                    >
                      <i class="fas fa-heart"></i>
                    </button-base>
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
        <div class="mx-auto">
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
import Paginator from "@/libs/Paginator";
import { rssUpwork as api } from "@/api";

export default {
  data() {
    return {
      color: "light",
      items: [],
      paginator: new Paginator(15),
      showedIds: [],
    };
  },
  components: {
    CardBase,
    ButtonBase,
    TableTd,
    PaginatorAdmin,
  },
  mounted() {
    this.getItems();
  },
  methods: {
    getItems() {
      api.jobsIndex(this.listQuery).then((response) => {
        this.items = response.results;
        this.paginator.setCount(response.count);
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
    markFavourite(ids, favourited) {
      const data = ids.map((id) => ({ id: id, favourited: favourited }));
      api.jobsMarkFavourite(data).then(() => {
        ids.forEach((id) => {
          let item = this.items.find((item) => item.id == id);
          if (item) {
            item.is_favourited = favourited;
          }
        });
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
  },
  computed: {
    listQuery() {
      return {
        offset: this.paginator.offset,
        limit: this.paginator.limit,
      };
    },
  },
};
</script>
