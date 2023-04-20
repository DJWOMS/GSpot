import Section from 'components/Section'
import { FaqInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'
import { notFound } from 'next/navigation'
import s from './page.module.scss'

const Page = async () => {
  const faq = await fetchServerSide<FaqInterface>({
    path: '/games/faq',
    cache: 'no-cache',
  })

  if (!faq) {
    notFound()
  }
  return (
    <>
      <Section title="FAQ" />

      <Section>
        <div className="container">
          <div className={s.row}>
            <div className={s.navColumn}>
              <div className={s.row}>
                <div className={s.filter}>
                  <h4 className={s.filterTitle}>Help center</h4>

                  <div className={s.filterGroup}>
                    <input type="text" className={s.filterInput} placeholder="Keyword" />
                  </div>

                  <div className={s.filterGroup}>
                    <label className={s.filterLabel}>Navigation:</label>
                    <ul className={s.filterNav}>
                      <li>
                        <a className={s.active} href="#">
                          All
                        </a>
                      </li>
                      <li>
                        <a href="#">GG.template</a>
                      </li>
                      <li>
                        <a href="#">Profile</a>
                      </li>
                      <li>
                        <a href="#">Categories</a>
                      </li>
                      <li>
                        <a href="#">Platforms</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <div className={s.info}>
              <div className={s.row}>
                <div className={s.infoFaq}>
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>GG.template</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                    </ul>
                  </div>
                </div>
                <div className={s.infoFaq}>
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>Profile</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                    </ul>
                  </div>
                </div>

                <div className={s.infoFaq}>
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>Categories</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                    </ul>
                  </div>
                </div>

                <div className={s.infoFaq}>
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>Platforms</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                      <li>
                        <a href="#">{faq.description}</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Section>
    </>
  )
}
export default Page
