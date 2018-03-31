<template>
  <div id="gallery">
    <div class="crumb">
      <div class="bread">
        <ol class="breadcrumb">
          <li>
            <a href="#">{{ galleries.name }}</a>
          </li>
        </ol>
      </div>
      <div class="action"></div>
    </div>
      <div class="row media-content">
        <div class="col-xs-6 col-md-3 thumb" v-bind:data-id="cet.id" v-for="(cet, key) in galleries.pictures" v-bind:key="key">
          <a href="#" class="thumbnail">
            <img v-bind:src="cet.content" alt="...">
          </a>
        </div>
        <!--{{ cet.name }}-->
      </div>
    <!--<header slot="folder_name"></header>-->
    <!--v-bind绑定属性-->
    <!--<div class="media-content">-->
      <!--<div v-bind:data-id="cet.id" v-for="(cet, key) in galleries.pictures" v-bind:key="key" class="thumb">-->
        <!--<figure itemprop="image">-->
          <!--<div class="multimedia">-->
          <!--<a href="##" v-bind:title="isPhoto">-->
            <!--{{ cet.name }}-->
            <!--<div>-->
            <!--<img v-bind:src="cet.content " alt="##" v-if="cet.type==='image' "-->
            <!--class="img-rounded"/>-->
            <!--<video src="##" v-else></video>-->
            <!--</div>-->
          <!--</a>-->
            <!--&lt;!&ndash;<div> 页面上的操作栏&ndash;&gt;-->
              <!--&lt;!&ndash;<div class="on-up-corer action"></div>&ndash;&gt;-->
              <!--&lt;!&ndash;<div class="down-bottom-corer action"></div>&ndash;&gt;-->
            <!--&lt;!&ndash;</div>&ndash;&gt;-->
        <!--</div>-->
        <!--</figure>-->
      <!--</div>-->
      <!--<div  class="thumb">-->
        <!--<figure itemprop="image">-->
          <!--<div class="multimedia">-->
            <!--<a href="##" v-bind:title="isPhoto">-->
              <!--<div>-->
                <!--<img src="https://images.unsplash.com/photo-1521402966881-852a3b2551fc" alt="##"-->
                     <!--class="img-rounded"/>-->
              <!--</div>-->
            <!--</a>-->
            <!--&lt;!&ndash;<div> 页面上的操作栏&ndash;&gt;-->
            <!--&lt;!&ndash;<div class="on-up-corer action"></div>&ndash;&gt;-->
            <!--&lt;!&ndash;<div class="down-bottom-corer action"></div>&ndash;&gt;-->
            <!--&lt;!&ndash;</div>&ndash;&gt;-->
          <!--</div>-->
        <!--</figure>-->
      <!--</div>-->
    <!--</div>-->
  </div>
</template>

<script>
import { getFolderContent } from '../../api/api'

export default {
  name: 'gallery',
  data () {
    return {
      'contents': {
        'id': '1'
      },
      'galleries': []
    }
  },
  // mounted 挂载可以获取el的dom元素
  created () {
    console.log('这个吗', this.$route.params)
    getFolderContent({ 'folder-id': this.$route.params.folder_id }).then(response => {
      this.galleries = response.data
    }).catch(error => {
      console.log(error)
    })
    console.log('cc', this.galleries)
  }
}
</script>

<style scoped>
  .row {
    position: relative;
  }
/*img {*/
  /*max-height: 300px;*/
  /*max-width: 300px;*/
  /*!*vertical-align: middle;*!*/
/*}*/

</style>
