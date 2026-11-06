import { defineConfig } from '@rspress/core';
import path from 'node:path';


export default defineConfig({

    globalStyles: path.join(__dirname, 'theme/var.css'),

    root: 'docs',
    base: '/',
    title: 'english-words',
    description: 'english-words',
    icon: '/favicon.ico',
    // logo: '/logo.png',
    logoText: 'english-words',

    markdown: {
        link: {
            checkDeadLinks: false,
        },
    },
    route: {
        cleanUrls: false,
    },

    // ===== 性能优化 =====
    builderConfig: {
        performance: {
            // split-by-size: 按体积合并小 chunk，减少 HTTP 请求数
            splitChunks: {
                strategy: 'split-by-size',
            },
        },
    },

    themeConfig: {
        search: false,
        // 关闭动画，减少 JS 体积
        enableContentAnimation: false,
        enableAppearanceAnimation: false,
        enableScrollToTop: true,
        lastUpdated: true,
        outlineTitle: '本页目录',
        prevPageText: '上一页',
        nextPageText: '下一页',
        lastUpdatedText: '最近更新时间',
        searchPlaceholderText: '搜索',
        sourceCodeText: '源码',
        overview: {
            filterNameText: '快速查找',
            filterPlaceholderText: '输入关键词',
            filterNoResultText: '未查询到结果',
        },
        socialLinks: [
            {
                icon: 'github',
                mode: 'link',
                content: 'https://github.com/mikigo/english-words/',
            }
        ],

        footer: {
            message: `版权所有 © 2023-${new Date().getFullYear()} mikigo`,
        },
        hideNavbar: 'auto',
    },
});