<template>
<div class="post-detail">
    <h1>Title:{{ post.title }}</h1>
    <div class="post-img">
        <img :src="post.img" alt="">
    </div>
    <div class="post-content">
        <h3>Content: {{ post.content }}</h3>
    </div>
</div>
</template>

<script>
export default {
  name: 'BlogPostCardDetail',
  props: {
    post: Object
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
