import Vue from "vue"
import VueRouter from "vue-router"

import Login from "../views/Login"
import Layout from "../views/Layout"
import Home from "../views/Home"
import News from "../views/News"
import NewsList from "../views/News/NewsList"
import NewsAdd from "../views/News/NewsAdd"
import NewsEdit from "@/views/News/NewsEdit"
import AudioPlayer from "@/views/News/AudioPlayer"




Vue.use(VueRouter)

const routes = [
    { path: "/login", name: "login", component: Login },
    {
        path: "/", component: Layout, children: [
            { path: "/", name: "home", component: Home },
            {
                path: "/news", component: News, children: [
                    { path: "", redirect: { name: "newsList" } },
                    { path: "list", name: "newsList", component: NewsList },
                    { path: "add", name: "newsAdd", component: NewsAdd },
                    { path: "edit", name: "newsEdit", component: NewsEdit },
                    { path: "player", name: "audioPlayer", component: AudioPlayer },
                ]
            }

        ]
    }
]


const router = new VueRouter({
    mode: "history",
    routes
})

export default router