import React from 'react'
import Section from 'components/Section'
import { SkeletonGameBigCard } from 'components/Skeleton'
import s from './loading.module.scss'

export default function Loading() {
  return (
    <Section>
      <div className={s.details}>
        <SkeletonGameBigCard />
        <div className={s.detailsText}>
          {[...new Array(10)].map((_, index) => (
            <div className={s.detailsTextLine} key={index} />
          ))}
        </div>
        <div className={s.detailsContent}>
          {[...new Array(7)].map((_, index) => (
            <div className={s.detailsContentLine} key={index} />
          ))}
        </div>
      </div>
    </Section>
  )
}
