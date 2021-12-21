<template>
    <div class="post-card">
        <h3>Category: {{ title }}</h3>
        <img :src="img" alt="" class='img-post' >
        <div class="post-category">
            <h4>Caregory: {{ category.title }}</h4>
        </div>
        <div class="post-description">
            <h4>Description: {{ description }}</h4>
        </div>
        <hr>
        <div class="post-tag" v-for="t in tag" :key="t.id" >
            <h5>#{{ t.title }}</h5>
        </div>
        <div class="post-tag">
            <a href="#" v-for="t in tag" :key="t.id" class="post-tag2"> #{{ t.title }} </a>
        </div>
        <div class="post-updadated_at">
            <h6>Updated_at: {{ updated_at }}</h6>
        </div>
        <a :href="`/post/${id}`">Read</a>
    </div>
</template>

<script>
export default {
  name: 'BlogPostCard',
  props: {
    id: Number,
    title: String,
    img: String,
    category: Object,
    description: String,
    tag: Object,
    updated_at: String
  }
}
</script>

<style scoped>
.post-card {
    background-color: rgb(44, 219, 123);
    bottom: 2px solid black;
    padding: 20px;
    margin: 20px;
    border-radius: 15px;
}
.img-post {
    width: 200px;
    height: 150px;
}
.post-tag2 {
    text-decoration: none;
}
</style>
