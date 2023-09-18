import { IconHeart, IconPlayerPlay } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import Section from 'components/Section'
import { Languages, Platform, Requirements } from 'features/games/components'
import type { GameDetailsInterface } from 'features/games/types'
import { CheckAge } from 'features/profile/components'
import { fetchServerSide } from 'lib/fetchServerSide'
import Image from 'next/image'
import { notFound } from 'next/navigation'
import s from './page.module.css'

const Page = async () => {
  const details = await fetchServerSide<GameDetailsInterface>({
    path: '/games/details/id',
    cache: 'no-cache',
  })

  if (!details) {
    notFound()
  }

  return (
    <Section>
      <div className="container">
        <CheckAge image={details.coverImg} age={details.age} />
        <div className="-mx-41">
          <div className="flex-1">
            <div className={s.details}>
              <div className={s.detailsHead}>
                <div className={s.detailsCover}>
                  <Image src={details.coverImg} width={240} height={340} alt="" />

                  <a href="..." className={s.detailsTrailer}>
                    <IconPlayerPlay />
                    <span>Watch trailer</span>
                  </a>
                </div>

                <div className={s.detailsWrap}>
                  <h3 className={s.detailsTitle}>{details.title}</h3>

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
                      <Languages>{details.languages}</Languages>
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
                    navigation={true}
                  >
                    {[...new Array(12)].map((_, index) => (
                      <img key={index} src="https://picsum.photos/1020" alt="" />
                    ))}
                  </Carousel>
                </div>
              </div>

              <div className={s.detailsText}>
                {details.description.split('\n').map((paragraph, index) => (
                  <p key={index}>{paragraph}</p>
                ))}
              </div>

              <div className={s.detailsCart}>
                <span className={s.detailsCartTitle}>Available on platforms:</span>
                <ul className={s.detailsPlatforms}>
                  <Platform type="ps" />
                  <Platform type="xbox" />
                  <Platform type="win" />
                  <Platform type="ap" />
                </ul>

                <div className={s.detailsPrice}>
                  <span>₽15.36</span>
                  <s>₽38.80</s>
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
                <Requirements>{details.requirements}</Requirements>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Section>
  )
}
export default Page
