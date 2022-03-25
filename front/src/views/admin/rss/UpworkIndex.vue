<template>
  <div class="w-full lg:w-12/12 px-4">
    <card-base>
      <template v-slot:header>
        <h6 class="text-blueGray-700 text-xl font-bold">Upwork RSS</h6>
        <router-link :to="{ name: 'admin.rss.upwork.create' }">
          <button-base>Create</button-base>
        </router-link>
      </template>
      <div class="block w-full overflow-x-auto">
        <table class="items-center w-full bg-transparent border-collapse">
          <thead>
            <tr>
              <table-th> ID </table-th>
              <table-th> Type </table-th>
              <table-th> Title </table-th>
              <table-th> Topic </table-th>
              <table-th> Query </table-th>
              <table-th> Active </table-th>
              <table-th> Actions </table-th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items" :key="item.id">
              <table-td> {{ item.id }} </table-td>
              <table-td> {{ item.type }} </table-td>
              <table-td> {{ item.title }} </table-td>
              <table-td> {{ item.topic }} </table-td>
              <table-td> {{ item.q }} </table-td>
              <table-td> {{ item.active }} </table-td>
              <table-td>
                <table-dropdown>
                  <table-dropdown-link @click="gotoForm(item)">
                    Update
                  </table-dropdown-link>
                  <table-dropdown-link @click="deleteItem(item)">
                    Delete
                  </table-dropdown-link>
                </table-dropdown>
              </table-td>
            </tr>
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
      paginator: new Paginator(10),
    };
  },
  components: {
    CardBase,
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
      api.index(this.listQuery).then((response) => {
        this.items = response.results;
        this.paginator.setCount(response.count);
      });
    },
    gotoForm(item) {
      this.$router.push({
        name: "admin.rss.upwork.edit",
        params: { id: item.id },
      });
    },
    deleteItem(item) {
      api.delete(item.id).then(() => {
        const index = this.items.findIndex((i) => i.id == item.id);
        if (index > -1) {
          this.items.splice(index, 1);
        }
      });
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
