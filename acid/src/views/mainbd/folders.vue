<template>
  <div class="mainbd">
    <!--<table class="table">-->
      <!--<tr>-->
        <!--<th>-->
          <!--<div class="checkbox">-->
            <!--<label>-->
              <!--<input type="checkbox" >-->
            <!--</label>-->
          <!--</div>-->
        <!--</th>-->
        <!--<th>-->
          <!--图册-->
        <!--</th>-->
        <!--<th>-->
          <!--创建时间-->
        <!--</th>-->
        <!--<th>-->
          <!--描述-->
        <!--</th>-->
      <!--</tr>-->
      <!--<tr v-for="folder in folderlist" v-bind:key="folder.id">-->
        <!--<td>-->
          <!--<div class="checkbox">-->
            <!--<label>-->
              <!--<input type="checkbox" >-->
            <!--</label>-->
          <!--</div>-->
        <!--</td>-->
        <!--<td>-->
          <!--<embed src="../../assets/gallery.svg" type="image/svg+xml">-->
          <!--{{ folder.name }}-->
        <!--</td>-->
        <!--<td>-->
          <!--{{ folder.create_time }}-->
        <!--</td>-->
        <!--<td>-->
          <!--......-->
        <!--</td>-->
      <!--</tr>-->
    <!--</table>-->
    <el-table
      ref="multipleTable"
      :data="folderlist"
      tooltip-effect="dark"
      highlight-current-row=true
      style="width: 100%"
      @selection-change="handleSelectionChange"
      @row-click="GotoGallery">
      <!--key 属性。理想的 key-->
      <!--v-for-对象-->
      <!--<div v-for="folder in folderlist" v-bind:key="folder.id">-->
        <!--<el-table-column-->
        <!--type="selection"-->
        <!--width="55">-->
        <!--</el-table-column>-->
        <!--<el-table-column-->
          <!--label="图册"-->
          <!--width="120">-->
          <!--&lt;!&ndash;<embed src="../../assets/gallery.svg" type="image/svg+xml">&ndash;&gt;-->
          <!--{{ folder.name }}-->
        <!--</el-table-column>-->
        <!--<el-table-column-->
        <!--label="创建时间"-->
        <!--width="120">-->
          <!--{{ folder.create_time }}-->
        <!--</el-table-column>-->
      <!--</div>-->
      <el-table-column
        type="selection"
        width="55">
      </el-table-column>
       prop 父组件给子组件传值
      <el-table-column
        prop="name"
        label="图册"
        width="120">

      </el-table-column>
      <el-table-column
        prop="creator"
        label="创建者"
        width="120">
      </el-table-column>
      <el-table-column
        prop="create_time"
        label="created"
        width="120">
        <template slot-scope="scope">}</template>
      </el-table-column>
      <el-table-column
        prop="desc"
        label="相关描述"
        show-overflow-tooltip>
      </el-table-column>
    </el-table>
    <div style="margin-top: 20px; max-width:400px">
      <el-button @click="toggleSelection([tableData3[1], tableData3[2]])">切换第二、第三行的选中状态</el-button>
      <el-button @click="toggleSelection()">取消选择</el-button>
    </div>
  </div>
</template>

<script>
// import { mapState } from 'vuex'
export default {
  name: 'folders',
  data () {
    return {
      tableData3: [{
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-08',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-06',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-07',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }],
      multipleSelection: []
    }
  },
  beforeCreate () {
    this.$store.dispatch('setFolder')
  },
  computed: {
    folderlist () {
      return this.$store.getters.folder_list.folder_list
    }
  },
  methods: {
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    GotoGallery (row) {
      console.log('row', row, '\n')
      // this.$router.push({name: 'gallery', params: { row.id }})
      this.$router.push({path: `/folder/${row.id}`})
    }
  }
}
</script>

<style scoped>
</style>
