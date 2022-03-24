<template>
  <div
    class="py-2"
    v-if="paginator.getPages().length == 1 ? showOnePage : true"
  >
    <nav class="block">
      <ul class="flex pl-0 rounded list-none flex-wrap">
        <li>
          <a
            href="#pablo"
            class="
              first:ml-0
              text-xs
              font-semibold
              flex
              w-8
              h-8
              mx-1
              p-0
              rounded-full
              items-center
              justify-center
              leading-tight
              relative
              border border-solid border-emerald-500
              bg-white
              text-emerald-500
            "
            @click.prevent="changePage(1)"
            v-if="paginator.getCurrentPage() > 2"
          >
            <i class="fas fa-chevron-left -ml-px"></i>
            <i class="fas fa-chevron-left -ml-px"></i>
          </a>
        </li>
        <li>
          <a
            href="#pablo"
            class="
              first:ml-0
              text-xs
              font-semibold
              flex
              w-8
              h-8
              mx-1
              p-0
              rounded-full
              items-center
              justify-center
              leading-tight
              relative
              border border-solid border-emerald-500
              bg-white
              text-emerald-500
            "
            @click.prevent="changePage(paginator.getCurrentPage() - 1)"
            v-if="paginator.getCurrentPage() > 1"
          >
            <i class="fas fa-chevron-left -ml-px"></i>
          </a>
        </li>

        <li v-for="page in paginator.getPages()" :key="page">
          <a
            href="#pablo"
            class="
              first:ml-0
              text-xs
              font-semibold
              flex
              w-8
              h-8
              mx-1
              p-0
              rounded-full
              items-center
              justify-center
              leading-tight
              relative
              border border-solid border-emerald-500
            "
            :class="[
              page == paginator.getCurrentPage()
                ? ['text-white', 'bg-emerald-500']
                : ['text-emerald-500', 'bg-white'],
            ]"
            @click.prevent="changePage(page)"
          >
            {{ page }}
          </a>
        </li>

        <li>
          <a
            href="#pablo"
            class="
              first:ml-0
              text-xs
              font-semibold
              flex
              w-8
              h-8
              mx-1
              p-0
              rounded-full
              items-center
              justify-center
              leading-tight
              relative
              border border-solid border-emerald-500
              bg-white
              text-emerald-500
            "
            @click.prevent="changePage(paginator.getCurrentPage() + 1)"
            v-if="paginator.getLastPage() > paginator.getCurrentPage()"
          >
            <i class="fas fa-chevron-right -mr-px"></i>
          </a>
        </li>
        <li>
          <a
            href="#pablo"
            class="
              first:ml-0
              text-xs
              font-semibold
              flex
              w-8
              h-8
              mx-1
              p-0
              rounded-full
              items-center
              justify-center
              leading-tight
              relative
              border border-solid border-emerald-500
              bg-white
              text-emerald-500
            "
            @click.prevent="changePage(paginator.getLastPage())"
            v-if="paginator.getLastPage() - paginator.getCurrentPage() > 1"
          >
            <i class="fas fa-chevron-right -mr-px"></i>
            <i class="fas fa-chevron-right -mr-px"></i>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>
<script>
import Paginator from "@/libs/Paginator";
export default {
  name: "paginator-admin",
  props: {
    paginator: {
      type: Paginator,
      required: true,
    },
    offset: {
      type: Number,
      default: 2,
    },
    showOnePage: {
      type: Boolean,
      default: false,
    },
  },
  computed: {},
  methods: {
    changePage(page) {
      this.paginator.setPage(page);
      this.$emit("paginate");
    },
  },
};
</script>
