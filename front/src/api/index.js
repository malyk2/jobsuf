import Request from "@/libs/Request";

const auth = {
  login(data) {
    return new Request(data).post("auth/login");
  },
  logout() {
    return new Request().post("auth/logout");
  },
  // register(data) {
  //   return new Request(data).post("/api/admin/auth/register");
  // },
  getMe() {
    return new Request().get("auth/me");
  },
  // forgotPassword(data) {
  //   return new Request(data).post("/api/admin/auth/password/forgot");
  // },
  // resetPassword(data) {
  //   return new Request(data).post("/api/admin/auth/password/reset");
  // },
  // verifyEmail(id, hash, query) {
  //   return new Request().setParams(query).get("/api/admin/auth/verify/" + id + "/" + hash);
  // },
}

const users = {
  index(query = {}) {
    return new Request().setParams(query).get("/api/admin/users");
  },
  create(data) {
    return new Request(data).post("/api/admin/users");
  },
  get(id) {
    return new Request().get("/api/admin/users/"+id);
  },
  update(id, data) {
    return new Request(data).post("/api/admin/users/"+id);
  },
  delete(id) {
    return new Request().delete("/api/admin/users/"+id);
  },
}

const rssUpwork = {
  index(query = {}) {
    return new Request().setParams(query).get("rss/upwork/");
  },
  create(data) {
    return new Request(data).post("rss/upwork/");
  },
  get(id) {
    return new Request().get("rss/upwork/"+id+"/");
  },
  update(id, data) {
    return new Request(data).put("rss/upwork/"+id+"/");
  },
  delete(id) {
    return new Request().delete("rss/upwork/"+id+"/");
  },
}

export {
  auth,
  users,
  rssUpwork,
};
