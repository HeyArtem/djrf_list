<template>
  <div class="home">
    <BlogPostList :posts='posts'/>
  </div>
</template>

<script>
// @ is an alias to /src
import BlogPostList from '@/components/Blog_app/BlogPostList'
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    BlogPostList
  },
  data () {
    return {
      posts: []
    }
  },
  methods: {
    async getBlogPost () {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/')
        this.posts = response.data
      } catch (e) {
        console.log('E R R O R   N I G G A !!!')
      }
    }
  },
  mounted () {
    this.getBlogPost()
  }
}
</script>
