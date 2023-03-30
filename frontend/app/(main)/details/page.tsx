import Section from 'components/Section'
import { IconBrandXbox, IconBrandWindows, IconBrandApple, IconHeart, IconPlayerPlay } from '@tabler/icons-react'
import { Content } from './content'
import cn from 'classnames'
import s from './details.module.scss'

export default function Page() {
    return (
        <>
            <Section
                first
                bg
                items={[
                    {
                        children: (
                            <div className="container">
                                <div className="flex flex-wrap -mx-4">
                                    <div className="max-w-full flex-1">
                                        <div className={s.details}>
                                            <div className={s.details__head}>
                                                <div className={s.details__cover}>
                                                    <img src="https://picsum.photos/1021" alt="" />
                                                    <a href="http://www.youtube.com/watch?v=0O2aH4XLbto" className={s.details__trailer}>
                                                        <IconPlayerPlay />
                                                        <span>Watch trailer</span>
                                                    </a>
                                                </div>

                                                <div className={s.details__wrap}>
                                                    <h3 className={s.details__title}>BioShock Infinite Complete Edition</h3>

                                                    <ul className={s.details__list}>
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
                                                            <table className={s.iksweb}>
                                                                <tr>
                                                                    <td></td>
                                                                    <th>Интерфейс</th>
                                                                    <th>Озвучка</th>
                                                                    <th>Субтитры</th>
                                                                </tr>
                                                                <tr>
                                                                    <th>русский</th>
                                                                    <td></td>
                                                                    <td></td>
                                                                    <td></td>
                                                                </tr>
                                                                <tr>
                                                                    <th>английский </th>
                                                                    <td></td>
                                                                    <td></td>
                                                                    <td></td>
                                                                </tr>
                                                                <tr>
                                                                    <th>aрмянский </th>
                                                                    <td></td>
                                                                    <td></td>
                                                                    <td></td>
                                                                </tr>
                                                                <tr>
                                                                    <th>aбхазский</th>
                                                                    <td></td>
                                                                    <td></td>
                                                                    <td></td>
                                                                </tr>
                                                            </table>
                                                            <a className={s.languages} href="">
                                                                Посмотреть все поддерживаемые языки
                                                                <span>(24)</span>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                            <div className={s.details__gallery}>
                                                <div className={cn(s.details__carousel, s.owl_carousel)} id="details__carousel">
                                                    <a href="img/details/1-1.jpg"></a>
                                                    <img src="https://picsum.photos/1020" alt="" />
                                                    <a href="img/details/2-2.jpg"></a>
                                                    <img src="https://picsum.photos/1022" alt="" />
                                                    <a href="img/details/3-3.jpg"></a>
                                                    <img src="https://picsum.photos/1023" alt="" />
                                                    <a href="img/details/4-4.jpg"></a>
                                                    <img src="https://picsum.photos/1024" alt="" />
                                                    <a href="img/details/5-5.jpg"></a>
                                                    <img src="https://picsum.photos/1025" alt="" />
                                                    <a href="img/details/6-6.jpg"></a>
                                                </div>

                                                <button
                                                    className="details__nav details__nav_prev"
                                                    data-nav="#details__carousel"
                                                    type="button"
                                                ></button>
                                                <button
                                                    className="details__nav details__nav--next"
                                                    data-nav="#details__carousel"
                                                    type="button"
                                                ></button>
                                            </div>
                                            <div className={s.details__text}>
                                                <p>
                                                    There are many variations of passages of Lorem Ipsum available, but the majority have suffered
                                                    alteration in some form, by injected humour, or randomised words which dont look even slightly
                                                    believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isnt
                                                    anything embarrassing hidden in the middle of text.
                                                </p>
                                                <p>
                                                    All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary,
                                                    making this the first true generator on the Internet. All the Lorem Ipsum generators on the
                                                    Internet tend to repeat predefined chunks as necessary, making this the first true generator on
                                                    the Internet. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as
                                                    necessary, making this the first true generator on the Internet.
                                                </p>
                                            </div>

                                            <div className={s.details__cart}>
                                                <span className={s.details__cart_title}>Available on platforms:</span>
                                                <ul className={s.details__platforms}>
                                                    <li className={s.xb}>
                                                        <IconBrandXbox />
                                                    </li>
                                                    <li className={s.wn}>
                                                        <IconBrandWindows />
                                                    </li>
                                                    <li className={s.ap}>
                                                        <IconBrandApple />
                                                    </li>
                                                </ul>

                                                <span className={s.details__cart_title}>PRICE</span>
                                                <div className={s.details__price}>
                                                    <span>$15.36</span>
                                                    <s>$38.80</s>
                                                    <b>60% OFF</b>
                                                </div>

                                                <div className={s.details__actions}>
                                                    <button className={s.details__buy}>Buy now</button>

                                                    <button className={s.details__favorite}>
                                                        <IconHeart />
                                                        Add to favorites
                                                    </button>
                                                </div>
                                            </div>

                                            <Content />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ),
                    },
                ]}
            />
        </>
    )
}
