import Section from 'components/Section'
import { GameCardInterface } from 'features/games'
import { ListGames } from 'features/games'
import { ArticleContent } from 'features/news'
import { Comments } from 'features/news'
import { SocialLink } from 'features/news'
import { Subscribe } from 'features/news'
import { RelatedNews } from 'features/news'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

const Page = async () => {
  const randomGames = await fetchServerSide<GameCardInterface[]>({ path: '/games/random', cache: 'no-cache' })

  return (
    <Section>
      <div className="container">
        <div className={s.article}>
          <div className={s.row}>
            <div className={s.colLeft}>
              <ArticleContent />
              <div className={s.links}>
                <SocialLink type="facebook" />
                <SocialLink type="twitter" />
                <SocialLink type="vk" />
              </div>
              <Comments />
            </div>
            <div className={s.colRight}>
              <div className={s.sidebar}>
                <div className={s.row}>
                  <div className={s.colSmall}>{randomGames && <ListGames>{randomGames}</ListGames>}</div>
                  <div className={s.colSmall}>
                    <Subscribe />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <RelatedNews />
    </Section>
  )
}
export default Page
