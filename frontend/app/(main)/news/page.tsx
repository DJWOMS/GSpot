import Breadcrumbs from 'components/Breadcrumbs'
import { FC } from 'react'
import PostItem from '../(components)/post-item/PostItem'
import Section from 'components/Section'
import s from './styles.module.scss'

const Page: FC = () => {
    return (
        <Section
            items={[
                {
                    title: 'Новости',
                    navigation: [
                        {
                            children: <Breadcrumbs items={[{ name: 'Новости' }]} />,
                        },
                    ],
                    children: (
                        <section className="section section--last section--catalog">
                            <div className="container">
                                <div className={s.sort}>
                                    <div className={s.filterGroup}>
                                        <label className={s.filterLabel} htmlFor="genres">
                                            Жанры:
                                        </label>
                                        <div className={s.filterSelectWrapper}>
                                            <select className={s.filterSelect} name="genres" id="genres">
                                                {['Все категории', 'Экшены', 'Эдвенчуры'].map((i: string, id: number) => (
                                                    <option className={s.option} key={id} value={id}>
                                                        {i}
                                                    </option>
                                                ))}
                                            </select>
                                        </div>
                                    </div>
                                    <div className={s.filterGroup}>
                                        <label className={s.filterLabel} htmlFor="sort">
                                            Сортировать по:
                                        </label>
                                        <div className={s.filterSelectWrapper}>
                                            <select className={s.filterSelect} name="sort" id="sort">
                                                {['Актуальность', 'Новейшие', 'Старые'].map((i: string, id: number) => (
                                                    <option className={s.option} key={id} value={id}>
                                                        {i}
                                                    </option>
                                                ))}
                                            </select>
                                        </div>
                                    </div>
                                    <div className={s.sortResults}>Найдено 123 постов</div>
                                </div>

                                <div className={s.columns}>
                                    {new Array(11).fill(0).map((_: number, id: number) => (
                                        <div className="col-md-6 col-xl-4" key={id}>
                                            <PostItem
                                                title={'Главные 20 CS:GO игроков of 2023 согласно to Gspot.tv'}
                                                imageSrc={'https://picsum.photos/240/340'}
                                                date={'2 часа назад'}
                                                category={'CS:GO'}
                                                size={'normal'}
                                                commentsCount={34}
                                                url={'#'}
                                            />
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </section>
                    ),
                },
            ]}
        />
    )
}

export default Page
