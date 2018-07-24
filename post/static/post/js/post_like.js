var like = new Vue({
  delimiters: ['{', '}'],
  el: '#post_like',
  data:{

    name : "biswanat"
  },
  method:{

  },
  computed:{

  },
  created(){
    this.$http.get('').than(function(data){

    })
  },
});
