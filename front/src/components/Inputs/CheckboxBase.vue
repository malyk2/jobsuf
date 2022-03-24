<template>
  <div class="relative w-full mb-3">
    <label
      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
      htmlFor="grid-password"
      v-if="label"
    >
      {{ label }}
    </label>
    <input
      type="checkbox"
      class="
        border-0
        px-3
        py-3
        text-blueGray-600
        bg-white
        rounded
        text-sm
        shadow
        focus:outline-none focus:ring
        ease-linear
        transition-all
        duration-150
      "
      :checked="modelValue"
      @change="runChange"
    />
    <p v-if="error" class="text-red-500 text-xs">
      {{ error }}
    </p>
  </div>
</template>
<script>
export default {
  name: "checkbox-base",
  props: {
    label: {
      default: null,
      type: String,
    },
    error: {
      default: "",
      type: String,
    },
    modelValue: {
      default: false,
      type: Boolean,
    },
  },
  methods : {
    runChange(e) {
      this.$emit('update:modelValue', e.target.checked)
    }
  }
};
</script>
