import Section from 'components/Section'
import { UserItem } from 'features/profile/components'
import { UserPublicDataInterface } from 'features/profile/types'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './/page.module.css'

const Page = async ({ params }: { params: { id: string } }) => {
  const userPublicContent = await fetchServerSide<UserPublicDataInterface>({
    path: `/user/${params.id}`,
    cache: 'no-cache',
  })

  if (!userPublicContent) {
    // notFound();
  }

  return (
    <Section title="Профиль">
      <section className={s.container}>
        <UserItem username={'Джон Роджер'} is_active={true} country={2}></UserItem>
      </section>
    </Section>
  )
}
export default Page
