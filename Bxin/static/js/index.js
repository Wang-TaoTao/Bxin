var vm = new Vue({
    el: '#app',
    // 修改Vue变量的读取语法，避免和django模板语法冲突
    delimiters: ['[[', ']]'],
    data: {
        host,
        f1_tab: 1, // 1F 标签页控制
        f2_tab: 1, // 2F 标签页控制
        f3_tab: 1, // 3F 标签页控制
        cart_total_count: 0, // 购物车总数量
        contents: [], // 购物车数据,
        username:'',
    },
    mounted(){
        // 获取购物车数据
        this.get_carts();
        this.username=getCookie('username');
        console.log(this.username);
    },
    methods: {
        // 获取购物车数据
        get_carts(){
            var url = this.host+'/movies/';
            axios.get(url, {
                    responseType: 'json',
                })
                .then(response => {
                    this.movies = response.data.contents;
                    this.cart_total_count = 0;
                    for(var i=0;i<this.carts.length;i++){
                        if (this.movies[i].name.length>25){
                            this.movies[i].name = this.movies[i].name.substring(0, 25) + '...';
                        }
                        this.cart_total_count += this.movies[i].count;
                    }
                })
                .catch(error => {
                    console.log(error.response);
                })
        }
    }
});
