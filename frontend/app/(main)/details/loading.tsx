import React from 'react'
import Section from 'components/Section'
import { SkeletonInput } from 'components/Skeleton'
import s from './loading.module.css'

export default function Loading() {
  return (
    <Section>
      <div className={s.details}>
        <div className={s.detailsCard}>
          <div className={s.detailsCardImg} />
          <div className={s.detailsCardDesc}>
            <div className={s.detailsCardDescTitle} />
            {[...new Array(5)].map((_, index) => (
              <div className={s.detailsCardDescText} key={index} />
            ))}
          </div>
          <div className={s.detailsCardInfo}>
            <div className={s.detailsCardInfoText} />
            {[...new Array(3)].map((_, index) => (
              <div className={s.detailsCardInfoTitle} key={index} />
            ))}
            <div className={s.detailsCardInfoText} />
            <div className={s.detailsCardInfoTitle} />
            {[...new Array(2)].map((_, index) => (
              <div className={s.detailsCardInfoBtn} key={index} />
            ))}
          </div>
        </div>

        <div className={s.detailsText}>
          {[...new Array(10)].map((_, index) => (
            <div className={s.detailsTextLine} key={index} />
          ))}
        </div>
        <div className={s.detailsContent}>
          <SkeletonInput size={'44'} />
          {[...new Array(7)].map((_, index) => (
            <div className={s.detailsContentLine} key={index} />
          ))}
        </div>
      </div>
    </Section>
  )
}
