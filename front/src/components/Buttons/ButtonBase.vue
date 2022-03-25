<template>
  <button
    class="
      font-bold
      uppercase
      text-xs
      rounded
      shadow
      hover:shadow-md
      outline-none
      focus:outline-none
      mr-1
      ease-linear
      transition-all
      duration-150
    "
    :class="[colorClasses, sizeClasses]"
    :type="type"
  >
    <slot></slot>
  </button>
</template>
<script>
export default {
  name: "button-base",
  props: {
    color: {
      default: "success",
      validator: function (value) {
        return ["success", "info", "danger"].indexOf(value) !== -1;
      },
    },
    size: {
      default: "regular",
      validator: function (value) {
        return ["large", "regular", "small", "mini"].indexOf(value) !== -1;
      },
    },
    type: {
      default: "button",
      validator: function (value) {
        return ["button", "submit"].indexOf(value) !== -1;
      },
    },
    disabled: {
      default: false,
      type: Boolean,
    },
  },
  computed: {
    colorClasses() {
      switch (this.color) {
        case "success":
          return ["bg-emerald-500", "text-white", "active:bg-emerald-600"];
        case "info":
          return ["bg-amber-500", "text-white", "active:bg-amber-600"];
        case "danger":
          return ["bg-red-500", "text-white", "active:bg-red-600"];
        default:
          return [];
      }
    },
    sizeClasses() {
      switch (this.size) {
        case "large":
          return ["px-8", "py-3"];  
        case "regular":
          return ["px-6", "py-3"];
        case "small":
          return ["px-4", "py-2"];
        case "mini":
          return ["px-2", "py-1"];
        default:
          return [];
      }
    },
  },
};
</script>
