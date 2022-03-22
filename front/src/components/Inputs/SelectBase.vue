<template>
  <div class="relative w-full mb-3">
    <label
      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
      htmlFor="grid-password"
      v-if="label"
    >
      {{ label }}
    </label>
    <select
      class="
        border-0
        px-3
        py-3
        placeholder-blueGray-300
        text-blueGray-600
        bg-white
        rounded
        text-sm
        shadow
        focus:outline-none focus:ring
        w-full
        ease-linear
        transition-all
        duration-150
      "
      :value="modelValue"
      @change="$emit('update:modelValue', $event.target.value)"
    >
      <option v-if="firstOption" :value="null">{{ firstOption }}</option>
      <option v-for="(option, index) in options" :key="index" :value="option">
        {{ option }}
      </option>
    </select>
    <p v-if="error" class="text-red-500 text-xs">
      {{ error }}
    </p>
  </div>
</template>
<script>
export default {
  name: "select-base",
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
      default: "",
      type: String,
    },
    options: {
      default: () => [],
      type: Array,
    },
    firstOption: {
      default: null,
      type: String
    }
  },
};
</script>
