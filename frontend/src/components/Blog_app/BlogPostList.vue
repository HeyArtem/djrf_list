<template>
  <div class="post-list">
    <BlogPostCard
    v-for="post in posts"
    :key="post.id"
    :id='post.id'
    :title='post.title'
    :img='post.img'
    :category='post.category'
    :description='post.description'
    :tag='post.tag'
    :updated_at='post.updated_at'
    />
  </div>
</template>

<script>
import BlogPostCard from '@/components/Blog_app/BlogPostCard'

export default {
  name: 'BlogPostList',
  components: {
    BlogPostCard
  },
  props: {
    posts: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
