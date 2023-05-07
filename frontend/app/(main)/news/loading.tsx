import React from 'react'
import Section from 'components/Section'
import { SkeletonCard, SkeletonInput, SkeletonTitle } from 'components/Skeleton'
import s from './page.module.scss'

export default function Loading() {
  return (
    <Section>
      <SkeletonTitle />
      <section className="section section--last section--catalog">
        <SkeletonInput size={'full'} />
        <div className={s.columns}>
          {[...new Array(11)].map((_, index) => (
            <SkeletonCard key={index} />
          ))}
        </div>
      </section>
    </Section>
  )
}
