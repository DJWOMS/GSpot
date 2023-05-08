import React from 'react'
import Section from 'components/Section'
import { SkeletonCard, SkeletonInput, SkeletonTitle } from 'components/Skeleton'
import s from './page.module.css'

export default function Loading() {
  return (
    <Section>
      <section className="section section--last section--catalog">
        <SkeletonTitle />
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
