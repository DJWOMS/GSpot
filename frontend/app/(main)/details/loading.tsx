import React from 'react'
import { IconHeart, IconPlayerPlay } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import Section from 'components/Section'
import { SkeletonGameBigCard } from 'components/Skeleton'
import { Languages, Platform } from 'features/games'
import s from './../page.module.scss'

export default function Loading() {
  return (
    <Section>
      <div className="container">
        <div className="-mx-41">
          <div className="flex-1">
            <div className={s.details}>
              <div className={s.detailsHead}>
                <div className={s.detailsCover}>
                  <a href="..." className={s.detailsTrailer}>
                    <IconPlayerPlay />
                    <span>Watch trailer</span>
                  </a>
                </div>

                <div className={s.detailsWrap}>
                  <h3 className={s.detailsTitle}></h3>
                  <SkeletonGameBigCard />
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
                    </li>
                  </ul>
                </div>
              </div>

              <div className={s.detailsText}></div>

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

              <div className={s.detailsContent}></div>
            </div>
          </div>
        </div>
      </div>
    </Section>
  )
}
