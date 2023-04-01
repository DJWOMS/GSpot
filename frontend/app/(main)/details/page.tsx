import { IconHeart, IconPlayerPlay, IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import cn from 'classnames'
import Carousel from 'components/Carousel'
import Section from 'components/Section'
import { Languages, Platform, Requirements } from 'features/games'
import s from './page.module.scss'

export default function Page() {
  return (
    <Section>
      <div className="container">
        <div className="-mx-41">
          <div className="flex-[0_0_100%]">
            <div className={s.details}>
              <div className={s.detailsHead}>
                <div className={s.detailsCover}>
                  <img src="https://picsum.photos/1021" alt="" />
                  <a href="http://www.youtube.com/watch?v=0O2aH4XLbto" className={s.detailsTrailer}>
                    <IconPlayerPlay />
                    <span>Watch trailer</span>
                  </a>
                </div>

                <div className={s.detailsWrap}>
                  <h3 className={s.detailsTitle}>BioShock Infinite Complete Edition</h3>

                  <ul className={s.detailsList}>
                    <li>
                      <span>Release date:</span> 03.24.2016
                    </li>
                    <li>
                      <span>Genres:</span> Action, Role Playing, Open World
                    </li>
                    <li>
                      <span>Developer:</span> Envato Game Dev
                    </li>
                    <li>
                      <span>Языки:</span>
                      <Languages />
                    </li>
                  </ul>
                </div>
              </div>

              <div className={s.detailsGallery}>
                <div className={s.detailsCarousel}>
                  <Carousel
                    breakpoints={{
                      0: {
                        slidesPerView: 2,
                      },
                      576: {
                        slidesPerView: 2,
                      },
                      768: {
                        slidesPerView: 3,
                      },
                      1200: {
                        slidesPerView: 5,
                      },
                    }}
                  >
                    {[...new Array(10)].map((_, index) => (
                      <img key={index} src="https://picsum.photos/1020" alt="" />
                    ))}
                  </Carousel>
                </div>

                <button className={cn(s.detailsNav, s.left)} type="button">
                  <IconArrowLeft />
                </button>
                <button className={cn(s.detailsNav, s.right)} type="button">
                  <IconArrowRight />
                </button>
              </div>

              <div className={s.detailsText}>
                <p>
                  There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected
                  humour, or randomised words which dont look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to
                  be sure there isnt anything embarrassing hidden in the middle of text.
                </p>
                <p>
                  All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator
                  on the Internet. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first
                  true generator on the Internet. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making
                  this the first true generator on the Internet.
                </p>
              </div>

              <div className={s.detailsCart}>
                <span className={s.detailsCartTitle}>Available on platforms:</span>
                <ul className={s.detailsPlatforms}>
                  <Platform type="ps" />
                  <Platform type="xbox" />
                  <Platform type="win" />
                  <Platform type="ap" />
                </ul>

                <span className={s.detailsCartTitle}>PRICE</span>
                <div className={s.detailsPrice}>
                  <span>$15.36</span>
                  <s>$38.80</s>
                  <b>60% OFF</b>
                </div>

                <div className={s.detailsActions}>
                  <button className={s.detailsBuy}>Buy now</button>

                  <button className={s.detailsFavorite}>
                    <IconHeart />
                    Add to favorites
                  </button>
                </div>
              </div>

              <div className={s.detailsContent}>
                <Requirements />
              </div>
            </div>
          </div>
        </div>
      </div>
    </Section>
  )
}
