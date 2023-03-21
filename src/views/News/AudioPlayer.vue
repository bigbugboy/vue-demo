<template>
    <div>

        <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="date" label="日期" width="180">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="180">
            </el-table-column>
            <el-table-column prop="address" label="操作">
                <template slot-scope="scope">
                    <i style="font-size: 30px;" class="el-icon-video-play" @click="handlePlay(scope.row)"></i>
                    <i style="font-size: 30px;" class="el-icon-video-play" @click="handleDownload(scope.row)"></i>
                </template>
            </el-table-column>
        </el-table>

        <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
            <audio :src="audioSrc" controls="controls" ref="audio">
                您的浏览器不支持 audio 标签。
            </audio>
        </el-dialog>
    </div>
</template>

<script>
import axios from 'axios'
import fileDownload from 'js-file-download'


export default {
    data() {
        return {
            audioSrc: "",
            dialogVisible: false,
            tableData: [{
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-04',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1517 弄'
            }, {
                date: '2016-05-01',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1519 弄'
            }, {
                date: '2016-05-03',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1516 弄'
            }]
        }
    },
    methods: {
        pauseMusic() {
            this.$refs.audio.pause()
        },

        handleClose(done) {
            this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                    this.pauseMusic()
                })
                .catch(_ => { });
        },
        handlePlay(row) {
            // todo: 根据 row.filepath 调api 下载资源
            axios.get("/api/music", { responseType: 'blob' }).then((response) => {
                let res = response.data
                console.log(res)
                let mp3Url = window.URL.createObjectURL(new Blob([response.data]))
                this.audioSrc = mp3Url
            })
            this.dialogVisible = true
        },
        handleDownload(row) {
            axios.get("/api/download", { responseType: 'blob' }).then((response) => {
                fileDownload(response.data, "abc.mp3")
            })
        },
    }

}
</script>

<style></style>