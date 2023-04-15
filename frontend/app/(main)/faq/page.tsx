import Section from 'components/Section'
import s from './page.module.scss'

const Page = () => {
  return (
    <>
      <Section title="FAQ" />

      <Section>
        <div className="container">
          <div className={s.rowCatalog}>
            <div className="col-lg-20  grid   w-full   grid-cols-12">
              <div className={s.filter}>
                <h4 className={s.filterTitle}>Help center</h4>

                <div className={s.filterGroup}>
                  <input type="text" className={s.filterInput} placeholder="Keyword" />
                </div>

                <div className={s.filterGroup}>
                  <label className={s.filterLabel}>Navigation:</label>
                  <ul className={s.filterNav}>
                    <li>
                      <a className="active" href="#">
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
                    <li>
                      <a href="#">Discounts</a>
                    </li>
                    <li>
                      <a href="#">Payment</a>
                    </li>
                    <li>
                      <a href="#">Delete account</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <div className="col-lg-80 w-full">
              <div className="row">
                <div className="col-12 col-lg-6">
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>GG.template</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">Many desktop publishing packages and web page?</a>
                      </li>
                      <li>
                        <a href="#">Various versions have evolved over the years?</a>
                      </li>
                      <li>
                        <a href="#">The point of using Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">The generated Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">All the Lorem Ipsum generators on the Internet?</a>
                      </li>
                    </ul>
                  </div>
                </div>

                <div className="col-12 col-lg-6">
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>Profile</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">Many desktop publishing packages and web page?</a>
                      </li>
                      <li>
                        <a href="#">Various versions have evolved over the years?</a>
                      </li>
                      <li>
                        <a href="#">The point of using Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">The generated Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">All the Lorem Ipsum generators on the Internet?</a>
                      </li>
                    </ul>
                  </div>
                </div>

                <div className="col-12 col-lg-6">
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>Categories</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">Many desktop publishing packages and web page?</a>
                      </li>
                      <li>
                        <a href="#">Various versions have evolved over the years?</a>
                      </li>
                      <li>
                        <a href="#">The point of using Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">The generated Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">All the Lorem Ipsum generators on the Internet?</a>
                      </li>
                    </ul>
                  </div>
                </div>

                <div className="col-12 col-lg-6">
                  <div className={s.faq}>
                    <h3 className={s.faqTitle}>Platforms</h3>
                    <ul className={s.faqList}>
                      <li>
                        <a href="#">Many desktop publishing packages and web page?</a>
                      </li>
                      <li>
                        <a href="#">Various versions have evolved over the years?</a>
                      </li>
                      <li>
                        <a href="#">The point of using Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">The generated Lorem Ipsum?</a>
                      </li>
                      <li>
                        <a href="#">All the Lorem Ipsum generators on the Internet?</a>
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
