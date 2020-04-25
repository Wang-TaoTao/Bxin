let vm = new Vue({
        el: '#app',
        delimiters: ['[[', ']]'],
        data: {
            hot_movie: [],
            movie_id: movie_id,
            tab_content: {
                detail: true,
                pack: false,
                comment: false,
                service: false
            },

            score_classes: {
                1: 'stars_one',
                2: 'stars_two',
                3: 'stars_three',
                4: 'stars_four',
                5: 'stars_five',
            },
        },
        mounted(){
            // 获取热播电影
            this.get_hot_skus();
          
        },
        methods: {  
            // 控制页面标签页展示
            on_tab_content(name){
                this.tab_content = {
                    detail: false,
                    pack: false,
                    comment: false,
                    service: false
                };
                this.tab_content[name] = true;
            },
            // 获取热播电影
            get_hot_skus(){
                if (this.movie_id) {
                    let url = '/hot/'+ this.movie_id +'/';
                    axios.get(url, {
                        responseType: 'json'
                    })
                        .then(response => {
                            this.hot_movie = response.data.hot_movie;
                            for(let i=0; i<this.hot_movie.length; i++){
                                this.hot_movie[i].url = '/detail/' + this.hot_movie[i].id + '/';
                            }
                        })
                        .catch(error => {
                            console.log(error.response);
                        })
                }
            },
            },
               
    });
