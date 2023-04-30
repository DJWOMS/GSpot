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
          <div className="grid grid-cols-3">
            <div className="col-span-3 lg:col-span-2">
              {articleContent && <ArticleContent>{articleContent}</ArticleContent>}
              <div className={s.links}>
                <SocialLink type="facebook" />
                <SocialLink type="twitter" />
                <SocialLink type="vk" />
              </div>
              {comments && <Comments>{comments}</Comments>}
            </div>
            <div className="col-span-3 lg:col-span-1">
              <div className={s.sidebar}>
                <div className="grid md:grid-cols-2 lg:grid-cols-1">
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
