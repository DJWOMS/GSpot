import Section from 'components/Section'
import { GameCardInterface } from 'features/games'
import { ListGames } from 'features/games'
import { ArticleContent, ArticleInterface, CommentInterface } from 'features/news'
import { Comments } from 'features/news'
import { SocialLink } from 'features/news'
import { Subscribe } from 'features/news'
import { RelatedNews } from 'features/news'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

const Page = async () => {
  const randomGames = await fetchServerSide<GameCardInterface[]>({ path: '/games/random', cache: 'no-cache' })
  const articleContent = await fetchServerSide<ArticleInterface>({ path: '/news/[id]', cache: 'no-cache' })
  const comments = await fetchServerSide<CommentInterface[]>({ path: '/news/comments', cache: 'no-cache' })

  return (
    <Section>
      <div className="container">
        <div className={s.article}>
          <div className={s.row}>
            <div className={s.colLeft}>
              {articleContent && <ArticleContent>{articleContent}</ArticleContent>}
              <div className={s.links}>
                <SocialLink type="facebook" />
                <SocialLink type="twitter" />
                <SocialLink type="vk" />
              </div>
              {comments && <Comments>{comments}</Comments>}
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