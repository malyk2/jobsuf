<template>
  <div class="flex flex-wrap">
    <div class="w-full lg:w-12/12 px-4">
      <card-base>
        <template v-slot:header>
          <h6 class="text-blueGray-700 text-xl font-bold">My secrets</h6>
        </template>
        <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
          <form @submit.prevent="save">
            <h6 class="text-blueGray-400 text-sm mt-3 mb-6 font-bold uppercase">
              Upwork Secrets
            </h6>
            <div class="flex flex-wrap">
              <div class="w-full lg:w-6/12 px-4">
                <input-base
                  label="org Uid"
                  v-model="form.org_uid"
                  :error="form.errors.first('org_uid')"
                />
              </div>
              <div class="w-full lg:w-6/12 px-4">
                <input-base
                  label="user Uid"
                  v-model="form.user_uid"
                  :error="form.errors.first('user_uid')"
                />
              </div>
              <div class="w-full lg:w-12 px-4">
                <input-base
                  label="security Token"
                  v-model="form.security_token"
                  :error="form.errors.first('security_token')"
                />
              </div>
            </div>
            <button-base type="submit" :disabled="form.busy">Save</button-base>
          </form>
        </div>
      </card-base>
    </div>
  </div>
</template>
<script>
import CardBase from "@/components/Cards/CardBase.vue";
import InputBase from "@/components/Inputs/InputBase.vue";
import ButtonBase from "@/components/Buttons/ButtonBase.vue";
import Form from "@/libs/Form";
import { rssUpwork as api } from "@/api";

export default {
  data() {
    return {
      form: new Form({
        org_uid: "",
        security_token: "",
        user_uid: "",
      }),
    };
  },
  components: {
    CardBase,
    InputBase,
    ButtonBase,
  },
  mounted() {
    api.getSecret().then((response) => {
      this.form.addParam(response);
    });
  },
  methods: {
    save() {
      this.form.errors.clear();
      this.form.busy = true;
      api
        .saveSecret(this.form.data())
        .then(() => {
        })
        .catch((response) => {
          this.form.onFail(response.data);
        });
    },
  },
};
</script>
