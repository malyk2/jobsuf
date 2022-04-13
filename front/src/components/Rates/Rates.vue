<template>
  <div class="absolute">
    <div class="bg-white border-0 rounded-">
      <ul class="flex justify-center items-center" @mouseleave="localRate = rate">
        <li v-for="index in count" :key="index">
          <rates-star
            :filled="index <= localRate ? true : false"
            class="text-yellow-500 hover:h-5 hover:w-5"
            @click="setRate(index)"
            @mouseover="localRate = index"
          />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import RatesStar from "@/components/Rates/RatesStar.vue";

export default {
  name: "rates-button",
  props: {
    count: {
      type: Number,
      required: false,
      default: 5,
    },
    rate: {
      type: Number,
      required: false,
      default: null,
    },
    defaultRate: {
      type: Number,
      required: false,
      default: null,
    },
  },
  data() {
    return {
      popoverShow: false,
      localRate: this.rate || this.defaultRate || 0,
    };
  },
  components: {
    RatesStar,
  },
  computed: {},
  methods: {
    setRate(index) {
      this.$emit("change", index);
    },
  },
};
</script>

<style>
</style>
