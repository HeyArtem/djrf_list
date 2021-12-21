<template>
  <div class="home">
    <BlogPostCardDetail :post='post'/>
  </div>
</template>

<script>
// @ is an alias to /src
import BlogPostCardDetail from '@/components/Blog_app/BlogPostCardDetail'
import axios from 'axios'

export default {
  name: 'BlogPostDetail',
  components: {
    BlogPostCardDetail
  },
  props: {
    id: String
  },
  data () {
    return {
      post: []
    }
  },
  methods: {
    async getBlogPost () {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/post/${this.id}/`)
        // console.log(response.data)
        this.post = response.data
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
