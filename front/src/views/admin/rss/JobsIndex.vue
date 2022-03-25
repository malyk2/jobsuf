<template>
  <div class="w-full lg:w-12/12 px-4">
    <card-base>
      <template v-slot:header>
        <h6 class="text-blueGray-700 text-xl font-bold">Jobs</h6>
      </template>
      <div class="block w-full overflow-x-auto">
        <table class="items-center w-full bg-transparent border-collapse">
          <thead>
            <!-- <tr>
              <table-th> Rss </table-th>
              <table-th> Title </table-th>
              <table-th> Rate </table-th>
              <table-th> Country </table-th>
              <table-th> Published </table-th>
              <table-th> Created </table-th>
            </tr> -->
          </thead>
          <tbody>
            <template v-for="item in items" :key="item.id">
              <tr
                :class="{ 'text-blueGray-400': item.is_readed_by_auth_user }"
                @click="toggleShowDetail(item.id)"
              >
                <table-td class="w-9/12">
                  {{ item.title }}
                  <a
                    :href="item.upwork_id"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <i class="fas fa-link text-sm"></i>
                  </a>
                </table-td>
                <table-td>
                  {{
                    item.rate_from
                      ? "$" + item.rate_from + "-$" + item.rate_to
                      : "No rate"
                  }}
                </table-td>
                <table-td> {{ item.created }} </table-td>
              </tr>
              <tr v-show="isShowedDetail(item.id)">
                <table-td v-html="item.content" colspan="2"> </table-td>
                <table-td>
                  <div>
                    <button-base color="info">
                      <i class="fas fa-link text-sm"></i>
                    </button-base>
                  </div>
                </table-td>
                <!-- <table-td>
                  {{ item.rss }}<br />
                  {{ item.country }}
                </table-td>
                <table-td> {{ item.published }} </table-td> -->
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
import CardHeader from "@/components/Cards/CardHeader.vue";
import CardBase from "@/components/Cards/CardBase.vue";
import ButtonBase from "@/components/Buttons/ButtonBase.vue";
import TableTh from "@/components/Table/TableTh.vue";
import TableTd from "@/components/Table/TableTd.vue";
import TableDropdown from "@/components/Dropdowns/TableDropdown.vue";
import TableDropdownLink from "@/components/Dropdowns/TableDropdownLink.vue";
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
    CardHeader,
    ButtonBase,
    TableDropdown,
    TableDropdownLink,
    TableTh,
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
    markAssRead(ids) {
      // const data = ids.map((id) => ({'id': id}))
      // api.jobsMarkAsRead(data).then((response) => {
      //   ids.forEach(id => {
      //     let item = this.items.find(i => {id == i.id})
      //     if(item) {
      //       item.is_readed_by_auth_user = true
      //     }
      //   });
      // });
      
    },
    toggleShowDetail(id) {
      if (this.isShowedDetail(id)) {
        const index = this.showedIds.indexOf(id);
        if (index > -1) {
          this.showedIds.splice(index, 1);
        }
      } else {
        this.showedIds.push(id);
        // console.log(this.items);
        let x = this.items.find(i => {id == i.id})

        console.log('Current');
        // console.log('Current');
        console.log(x);
        // console.log(item.is_readed_by_auth_user);
        // item
        // if(item && !item.is_readed_by_auth_user) {
        //   this.markAssRead([id])
        // }
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
