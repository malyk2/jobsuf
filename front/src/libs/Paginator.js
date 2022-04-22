class Paginator {
  /**
   * Create a new Paginator instance.
   */
  constructor(limit = 10, offset = 0) {
    this.count = 0;
    this.limit = limit;
    this.offset = offset;
    this.pages = [];
  }

  createPaginator(count) {
    this.count = count
    this.fillPages();
    return this
  }

  fillPages() {
    const limit = this.limit * 1
    let pages = []
    let k = 1;
    
    for (let i = 0; i < this.count; i += limit) {
      pages.push(k)
      k++;
    }
    if (pages.length * limit < this.count) {
      pages.push(k)
    }
    this.pages = pages;
    return this
  }

  setPage(page) {
    this.offset = page > 1 ? (page - 1) * this.limit : 0
    return this
  }

  getCurrentPage() {
    return (this.offset / this.limit) + 1;
  }

  getLastPage() {
    const pages = this.getAllPages();
    return pages.length ? pages[pages.length - 1] : 1;
  }

  getAllPages() {
    return this.pages;
  }

  getPaginatorPages(showLimit=null) {
    let pages = []

    if(showLimit) {
      const lastPage = this.getLastPage()
      let from = this.getCurrentPage() - showLimit;
      if (from < 1) {
        from = 1;
      }
      let to = from + showLimit * 2;
      if (to >= lastPage) {
        to = lastPage;
      }
      for (let page = from; page <= to; page++) {
        pages.push(page);
      }
    } else {
      pages = this.getAllPages()
    }
    return pages;
  }
}

export default Paginator;
