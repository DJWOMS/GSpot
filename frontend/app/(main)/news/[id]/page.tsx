import Section from 'components/Section'
import { GameCardInterface } from 'features/games'
import { ArticleContent } from 'features/news/components/ArticleContent'
import { RandomGamesList } from 'features/news/components/RandomGamesList'
import { SocialLink } from 'features/news/components/SocialLink'
import { Subscribe } from 'features/news/components/Subscribe'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

const Page = async () => {
  const randomGames = await fetchServerSide<GameCardInterface[]>({ path: '/games/random' })

  return (
    <Section>
      <div className="container">
        <div className={s.article}>
          <div className={s.row}>
            <div className={s.colLeft}>
              <ArticleContent s={s} />
              <div className={s.links}>
                <SocialLink type="facebook" />
                <SocialLink type="twitter" />
                <SocialLink type="vk" />
              </div>
            </div>
            <div className={s.colRight}>
              <div className={s.sidebar}>
                <div className={s.row}>
                  <div className={s.colSmall}>{randomGames && <RandomGamesList>{randomGames}</RandomGamesList>}</div>
                  <div className={s.colSmall}>
                    <Subscribe />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Section>
  )
}
export default Page
