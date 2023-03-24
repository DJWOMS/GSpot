import s from './FilterGames.module.scss'

export function FilterGames() {
    return (
        <div className="filter-wrap">
            <button className={s.openFilter}>Открыть фильтр</button>

            <div className={s.wrapper}>
                <div className={s.components}>
                    <h4 className={s.title}>
                        Фильтры <button className={s.clearFilters}>Очистить</button>
                    </h4>

                    <div className={s.group}>
                        <label className={s.label}>Ключевые слова: </label>
                        <input className={s.input} type="text" placeholder="Keyword" />
                    </div>

                    <div className={s.group}>
                        <label className={s.label}>Сортировать: </label>

                        <div className={s.selectWrap}>
                            <select className={s.select}>
                                <option value="0">По интересам</option>
                                <option value="1">От новых к старым</option>
                                <option value="2">От старых к новым</option>
                            </select>
                        </div>
                    </div>

                    <div className={s.group}>
                        <label className={s.label}>Цена: </label>

                        <div className={s.range}>
                            <div id="filter__range-start"></div>
                            <div id="filter__range-end"></div>
                        </div>

                        <div className={s.range} />
                    </div>

                    <div className={s.group}>
                        <label className={s.label}>Платформа: </label>
                        <ul className={s.checkboxes}>
                            <li className={s.checkbox}>
                                <input id="type1" type="checkbox" name="type1" defaultChecked />
                                <label htmlFor="type1">Playstation</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type2" type="checkbox" name="type2" />
                                <label htmlFor="type2">XBOX</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type3" type="checkbox" name="type3" />
                                <label htmlFor="type3">Windows</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type4" type="checkbox" name="type4" />
                                <label htmlFor="type4">Mac OS</label>
                            </li>
                        </ul>
                    </div>

                    <div className={s.group}>
                        <label className={s.label}>Жанры:</label>
                        <ul className={s.checkboxes}>
                            <li className={s.checkbox}>
                                <input id="type5" type="checkbox" name="type5" defaultChecked />
                                <label htmlFor="type5">Action</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type6" type="checkbox" name="type6" />
                                <label htmlFor="type6">Adventure</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type7" type="checkbox" name="type7" defaultChecked />
                                <label htmlFor="type7">Fighting</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type8" type="checkbox" name="type8" defaultChecked />
                                <label htmlFor="type8">Flight simulation</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type9" type="checkbox" name="type9" />
                                <label htmlFor="type9">Platform</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type10" type="checkbox" name="type10" />
                                <label htmlFor="type10">Racing</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type11" type="checkbox" name="type11" />
                                <label htmlFor="type11">RPG</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type12" type="checkbox" name="type12" />
                                <label htmlFor="type12">Sports</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type13" type="checkbox" name="type13" />
                                <label htmlFor="type13">Strategy</label>
                            </li>
                            <li className={s.checkbox}>
                                <input id="type14" type="checkbox" name="type14" />
                                <label htmlFor="type14">Survival horror</label>
                            </li>
                        </ul>
                    </div>

                    <div className={s.group}>
                        <button className={s.applyFilter}>Применить фильтр</button>
                    </div>
                </div>
            </div>
        </div>
    )
}
