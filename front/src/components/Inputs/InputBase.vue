<template>
  <div class="relative w-full mb-3">
    <label
      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
      htmlFor="grid-password"
      v-if=label
    >
      {{ label }}
    </label>
    <input
      :type="type"
      class="
        border-0
        placeholder-blueGray-300
        text-blueGray-600
        bg-white
        rounded
        text-sm
        shadow
        focus:outline-none
        focus:ring
        w-full
        ease-linear
        transition-all
        duration-150
      "
      :class="[sizeClasses]"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
    <p
      v-if="error"
      class="text-red-500 text-xs"
    >
      {{ error }}
    </p>
  </div>
</template>
<script>
export default {
  name: "input-base",
  props: {
    label: {
      default: null,
      type: String,
    },
    type: {
      default: "text",
      type: String,
      validator: function (value) {
        // The value must match one of these strings
        return ["text", "password","date"].indexOf(value) !== -1;
      },
    },
    size: {
      default: "regular",
      type: String,
      validator: function (value) {
        return ["regular", "small", "mini"].indexOf(value) !== -1;
      },
    },
    error: {
      default: "",
      type: String,
    },
    modelValue: {
      default: "",
      type: String,
    },

  },
  computed: {
    sizeClasses() {
      switch (this.size) {
        case "regular":
          return ["px-3", "py-3"];
        case "small":
          return ["px-2", "py-2"];
        case "mini":
          return ["px-1", "py-1"];
        default:
          return [];
      }
    },
  }
};
</script>
