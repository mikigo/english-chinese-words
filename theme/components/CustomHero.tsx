import React from 'react';

interface CustomHeroProps {
  name: string;
  text: string;
  tagline: string;
  categoryCount: number;
}

/** lixiaolai.com 风格双栏 Hero */
const CustomHero: React.FC<CustomHeroProps> = ({ name, text, tagline, categoryCount }) => {
  return (
    <div className="custom-hero">
      {/* 左侧：主标题 */}
      <div className="custom-hero__main">
        <h1 className="custom-hero__title">{name}</h1>
        <p className="custom-hero__en">English-Chinese Vocabulary</p>
        <p className="custom-hero__sub">{text}</p>
        <p className="custom-hero__desc">{tagline}</p>

        <div className="custom-hero__stats">
          <div className="custom-hero__stat">
            <span className="custom-hero__stat-num">{categoryCount}</span>
            <span className="custom-hero__stat-label">词库分类</span>
          </div>
          <div className="custom-hero__stat">
            <span className="custom-hero__stat-num">免费</span>
            <span className="custom-hero__stat-label">完全开放</span>
          </div>
        </div>

        <div className="custom-hero__links">
          <a href="/四级/" className="custom-hero__link">
            开始背单词 <span className="custom-hero__link-arrow">→</span>
          </a>
          <a href="https://github.com/mikigo/english-words/" target="_blank" rel="noopener noreferrer" className="custom-hero__link">
            GitHub <span className="custom-hero__link-arrow">↗</span>
          </a>
        </div>
      </div>

      {/* 右侧：简介卡片 */}
      <aside className="custom-hero__card">
        <p style={{ margin: '0 0 12px', color: 'var(--rp-c-text-2)', fontSize: '0.875rem', lineHeight: 1.7 }}>
          覆盖<strong>四级、六级、考研、雅思、托福、GRE、GMAT、SAT</strong>等主流考试，
          以及<strong>人教版、北师大版、外研社版</strong>中小学教材词汇。
        </p>
        <p style={{ margin: '0 0 12px', color: 'var(--rp-c-text-2)', fontSize: '0.875rem', lineHeight: 1.7 }}>
          同时收录<strong>专四、专八、中考、高考、商务英语、新东方</strong>等词库，
          以及<strong>Ogden's Basic English 850</strong>基础核心词汇。
        </p>
        <p style={{ margin: 0, color: 'var(--rp-c-text-3)', fontSize: '0.75rem' }}>
          数据来源：有道词典 · 精心整理
        </p>
      </aside>
    </div>
  );
};

export default CustomHero;