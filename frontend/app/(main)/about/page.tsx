import Carousel from 'components/Carousel'
import Section from 'components/Section'
import s from './page.module.css'

interface partner {
  link: string
  img: string
}
const partners: partner[] = [
  { link: '#', img: '/partners/activeden.png' },
  { link: '#', img: '/partners/audiojungle.png' },
  { link: '#', img: '/partners/codecanyon.png' },
  { link: '#', img: '/partners/docean.png' },
  { link: '#', img: '/partners/photodune.png' },
  { link: '#', img: '/partners/themeforest.png' },
]

const AboutPage = () => {
  return (
    <Section>
      <div className={s.sectionWrap}>
        <img src="/partners/about.jpg" alt="картинка" className={s.img} />
        <div className={s.wrapper}>
          <div className={s.contentWrap}>
            <h1 className={s.headingText}>Keep Reading</h1>
            <p className={s.descriptionText}>
              It is a long established fact that a reader will be distracted by the readable content of a page
              when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal
              distribution of letters, as opposed to using Content here, content here, making it look like
              readable English.
            </p>
            <p className={s.descriptionText}>
              Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model
              text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various
              versions have evolved over the years, sometimes by accident, sometimes on purpose injected
              humour and the like.
            </p>
          </div>

          <div className={s.contentWrap}>
            <h2 className={s.headingText}>Keep Reading</h2>
            <p className={s.descriptionText}>
              There are many variations of passages of Lorem Ipsum available, but the majority have suffered
              alteration in some form, by injected humour, or randomised words which don&acute;t look even
              slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there
              isn&acute;t anything embarrassing hidden in the middle of text.
            </p>
          </div>
        </div>
      </div>

      <div className={s.carouselWrap}>
        <Carousel
          breakpoints={{
            0: {
              slidesPerView: 2,
            },
            576: {
              slidesPerView: 2,
            },
            768: {
              slidesPerView: 4,
            },
            1200: {
              slidesPerView: 6,
            },
          }}
        >
          {partners.map((par, index) => {
            return (
              <a href={par.link} className={s.imageCarousel} key={index}>
                <img src={par.img} alt="картинка" />
              </a>
            )
          })}
        </Carousel>
      </div>
    </Section>
  )
}

export default AboutPage
