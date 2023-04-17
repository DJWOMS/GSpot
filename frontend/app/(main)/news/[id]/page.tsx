import Section from 'components/Section'
import ArticleContent from 'features/news/components/ArticleContent/ArticleContent'
import s from './page.module.scss'

const Page = async () => {
  return (
    <Section>
      <div className="container">
        <div className={s.article}>
          <div className="row">
            <div className="col-12 col-xl-8">
              <ArticleContent s={s} />
            </div>
          </div>
        </div>
      </div>
    </Section>
  )
}
export default Page
