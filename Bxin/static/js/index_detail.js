let vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        username: getCookie('username'),
        hot_skus: [],
        tab_content: {

	    detail: true,
            pack: false,
            comment: false,
            service: false
        
},
        cart_total_count: 0,
        carts: [],
        comments: [],
        count:[],
   
},
    mounted(){
		// 获取热销商品数据
        this.get_hot_skus();
  
   
    methods: {
        
    	// 获取热销商品数据
        get_hot_skus(){
            if (this.category_id) {
                let url = '/hot/'+ this.category_id +'/';
                axios.get(url, {
                    responseType: 'json'
                })
                    .then(response => {
                        this.hot_skus = response.data.hot_skus;
                        for(let i=0; i<this.hot_skus.length; i++){
                            this.hot_skus[i].url = '/detail/' + this.hot_skus[i].id + '/';
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
            }
        },
