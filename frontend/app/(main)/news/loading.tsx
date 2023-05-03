import React from 'react'
import Section from 'components/Section'
import { SkeletonCard } from 'components/Skeleton'
import s from './page.module.scss'

export default function Loading() {
  return (
    <Section title="Новости">
      <section className="section section--last section--catalog">
        <div className={s.columns}>
          {[...new Array(11)].map((_, index) => (
            <SkeletonCard key={index} />
          ))}
        </div>
      </section>
    </Section>
  )
}
