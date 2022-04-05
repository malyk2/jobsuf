<template>
  <div class="w-full lg:w-12/12 px-4">
    <card-base>
      <template v-slot:header>
        <h6 class="text-blueGray-700 text-xl font-bold">
          {{ id ? "Update" : "Create" }} upwork RSS
        </h6>
      </template>
      <form @submit.prevent="save">
        <div class="flex flex-wrap">
          <div class="w-full lg:w-6/12 px-4">
            <input-base
              label="Title"
              v-model="form.title"
              :error="form.errors.first('title')"
            />
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <select-base
              label="Type"
              v-model="form.type"
              :options="types"
              firstOption="Select type"
              :error="form.errors.first('type')"
            />
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <select-base
              label="Topic"
              v-model="form.topic"
              :options="topics"
              firstOption="Select topic"
              :error="form.errors.first('topic')"
            />
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <input-base
              label="Query"
              v-model="form.q"
              :error="form.errors.first('q')"
            />
          </div>
          <div class="w-full lg:w-3/12 px-4">
            <checkbox-base
              label="Acive"
              v-model="form.active"
              :error="form.errors.first('active')"
            />
          </div>
          <div class="w-full lg:w-3/12 px-4">
            <checkbox-base
              label="Public"
              v-model="form.public"
              :error="form.errors.first('public')"
            />
          </div>
        </div>
        <button-base type="submit" :disabled="form.busy">Save</button-base>
      </form>
    </card-base>
  </div>
</template>
<script>
import CardBase from "@/components/Cards/CardBase.vue";
import InputBase from "@/components/Inputs/InputBase.vue";
import SelectBase from "@/components/Inputs/SelectBase.vue";
import CheckboxBase from "@/components/Inputs/CheckboxBase.vue";
import ButtonBase from "@/components/Buttons/ButtonBase.vue";
import { rssUpwork as api } from "@/api";
import Form from "@/libs/Form";

export default {
  props: {
    id: {
      default: null,
      type: String,
    },
  },
  data() {
    return {
      form: new Form({
        title: "",
        type: "",
        topic: null,
        q: "",
        active: false,
        public: false,
      }),
      types: ["topics", "jobs"],
      topics: ["most-recent", "best-matches"],
    };
  },
  components: {
    CardBase,
    InputBase,
    SelectBase,
    CheckboxBase,
    ButtonBase,
  },
  mounted() {
    if (this.id) {
      if (this.id * 1 == this.id) {
        api
          .get(this.id)
          .then((response) => {
            const data = response;
            this.form.addParam(data);
          })
          .catch(() => {
            this.goToList();
          });
      } else {
        this.goToList();
      }
    }
  },
  methods: {
    save() {
      this.form.errors.clear();
      this.form.busy = true;
      const data = this.form.data();
      let request;
      if (!this.id) {
        request = api.create(data);
      } else {
        request = api.update(this.id, data);
      }
      request
        .then(() => {
          this.goToList();
        })
        .catch((response) => {
          this.form.onFail(response.data);
        });
    },
    goToList() {
      this.$router.push({ name: "admin.rss.upwork.index" });
    },
  },

  computed: {},
};
</script>
