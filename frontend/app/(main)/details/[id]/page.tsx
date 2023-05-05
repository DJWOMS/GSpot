'use client'

import { useEffect, useState } from 'react'
import { IconHeart, IconPlayerPlay } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import Section from 'components/Section'
import { GameDetailsInterface, Languages, Platform, Requirements } from 'features/games'
import { CheckAge } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import Image from 'next/image'
import Link from 'next/link'
import s from './page.module.scss'

const Page = async () => {
  const [age, setAge] = useState(true)

  const changeAge = () => {
    setAge(false)
  }

  const details = await fetchServerSide<GameDetailsInterface>({
    path: '/games/details/id',
    cache: 'no-cache',
  })

  useEffect(() => {
    if (typeof window === 'undefined') {
      console.log(age)
    }
  }, [age])

  return (
    <>
      {details.age === 'Adult' && age ? (
        <CheckAge image={details.coverImg} changeAge={changeAge} age={age} />
      ) : (
        <Section>
          <div className="container">
            <div className="-mx-41">
              <div className="flex-1">
                <div className={s.details}>
                  <div className={s.detailsHead}>
                    <div className={s.detailsCover}>
                      <Image src={details.coverImg} width={240} height={340} alt="" />
                      <Link href="..." className={s.detailsTrailer}>
                        <IconPlayerPlay />
                        <span>Watch trailer</span>
                      </Link>
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
                          <div>Языки:</div>
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
                    <Requirements>{details.requirements}</Requirements>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Section>
      )}
    </>
  )
}
export default Page
