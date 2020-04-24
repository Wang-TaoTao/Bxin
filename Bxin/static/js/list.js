var vm = new Vue({
    el: '#app',
    // 修改Vue变量的读取语法，避免和django模板语法冲突
    delimiters: ['[[', ']]'],
    data: {
        host,
        cart_total_count: 0, // 购物车总数量
        movies: [], // 购物车数据,
        hots: [],
        category_id: category_id,
        username: '',
    },
    mounted(){
        // 获取购物车数据
        this.get_carts();

        // 获取热销商品数据
        this.get_hot_goods();

        this.username = getCookie('username');
    },
    methods: {
        // 获取购物车数据
        get_carts(){
            var url = this.host + '/movies/';
            axios.get(url, {
                responseType: 'json',
            })
                .then(response => {
                    this.movies = response.data.movies;
                    this.cart_total_count = 0;
                    for (var i = 0; i < this.carts.length; i++) {
                        if (this.movies[i].name.length > 25) {
                            this.movies[i].name = this.movies[i].name.substring(0, 25) + '...';
                        }
                        this.cart_total_count += this.movies[i].count;
                    }
                })
                .catch(error => {
                    console.log(error.response);
                })
        },
        // 获取热销商品数据
        get_hot_goods(){
            var url = this.host + '/hotmovie/' + '/';
            axios.get(url, {
                responseType: 'json'
            })
                .then(response => {
                    this.hots = response.data.movies;
                    for (var i = 0; i < this.hots.length; i++) {
                        this.hots[i].url = '/goods/' + this.hots[i].id + '.html';
                    }
                })
                .catch(error => {
                    console.log(error.response);
                })
        }
    }
});
