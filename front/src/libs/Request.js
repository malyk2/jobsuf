import axios from 'axios';
// import Toastr from './Toastr';
// import router from '@/router';

class Request {
  /**
   * Create a new Form instance.
   *
   * @param {object} data
   */
  constructor(data = {}) {
    this.data = data;
    this.params = {};
    self = this
  }

  setParams(params = {}) {
    this.params = params;
    return this;
  }

  /**
   * Send a GET request to the given URL.
   * .
   * @param {string} url
  */
  get(url) {
    return this.send('get', url);
  }

  /**
   * Send a POST request to the given URL.
   * .
   * @param {string} url
   */
  post(url) {
    return this.send('post', url);
  }


  /**
   * Send a PUT request to the given URL.
   * .
   * @param {string} url
   */
  put(url) {
    return this.send('put', url);
  }


  /**
   * Send a PATCH request to the given URL.
   * .
   * @param {string} url
   */
  patch(url) {
    return this.send('patch', url);
  }


  /**
   * Send a DELETE request to the given URL.
   * .
   * @param {string} url
   */
  delete(url) {
    return this.send('delete', url);
  }

  send(requestType, uri) {
    axios.defaults.withCredentials = true;
    return new Promise((resolve, reject) => {
      axios({
        url: this.getUrl(uri),
        method: requestType,
        data: this.data,
        params: this.params
      }).then((response) => {
        // const message = response.data.message || null;
        // if (message) {
        //   Toastr.s(message);
        // }
        resolve(response.data);
      })
        .catch((error) => {
          reject(error.response);
        });
    });
  }

  getUrl(uri) {
    let url = process.env.VUE_APP_API_URL || 'http://localhost';
    const port = process.env.VUE_APP_API_PORT || false;
    url += port ? ':' + port + '/' + uri : '/' + uri
    return url
  }

  async csrf() {
    // return this
    return this.get('auth/csrf')
    // if (!this.getCookie('crrg')) {
    // } else {
    //   return this;
    // }
  }

  getCookie(name) {
    let cookie = {};
    document.cookie.split(';').forEach(function(el) {
      let [k,v] = el.split('=');
      cookie[k.trim()] = v;
    })
    return cookie[name];
  }
}

export default Request;
