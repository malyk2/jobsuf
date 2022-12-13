<template>
  <div class="relative w-full mb-3">
    <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlFor="grid-password" v-if="label">
      {{ label }}
    </label>
    <select class="
        border-0
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
      " :class=[sizeClasses] :value="modelValue" @change="$emit('update:modelValue', $event.target.value)">
      <slot v-if="slotOptions" />
      <template v-else>
        <option v-if="firstOption" :value="null">{{ firstOption }}</option>
        <template v-if="optionsType == 'array'">
          <option v-for="(option, index) in options" :key="index" :value="option">
            {{ option }}
          </option>
        </template>
        <template v-else-if="optionsType == 'objects'">
          <option v-for="(option, index) in options" :key="index" :value="option[optionValueType]">
            {{ option[optionTitleType] }}
          </option>
        </template>
      </template>
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
    size: {
      default: "regular",
      type: String,
      validator: function (value) {
        return ["regular", "small", "mini"].indexOf(value) !== -1;
      },
    },
    options: {
      default: () => [],
      type: Array,
    },
    optionsType: {
      default: "array",
      type: String,
      validator: function (value) {
        return ["array", "objects"].indexOf(value) !== -1;
      },
    },
    optionValueType: {
      default: "id",
      type: String,
    },
    optionTitleType: {
      default: "title",
      type: String,
    },
    firstOption: {
      default: null,
      type: String,
    },
    slotOptions: {
      default: false,
      type: Boolean,
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
