import typing as t

__all__ = ['Operator', 'OpExprConstructor', 'binop_reduce']


class Doubly:
    l: t.Optional['Doubly']
    v: object
    r: t.Optional['Doubly']

    def __init__(self, left, value, right):
        self.l = left
        self.v = value
        self.r = right


OpExprConstructor = t.Callable[[str], t.Callable[[object, object], object]]


class Operator:
    def __init__(self, opname):
        self.opname = opname


def chunk_by(f, seq):
    if not seq:
        return []
    seq = iter(seq)
    chunk = [next(seq)]
    last = f(chunk[0])
    chunks = []
    for each in seq:
        cur = f(each)
        if cur == last:
            chunk.append(each)
        else:
            chunks.append((last, chunk))
            chunk = [each]
        last = cur

    chunks.append((last, chunk))
    return chunks


def binop_reduce(cons: OpExprConstructor, seq: list,
                 precedences: t.Dict[str, int],
                 associativities: t.Dict[str, bool]):
    start = Doubly(None, None, None)
    last = start
    ops: t.List[Doubly] = []
    for each in seq:
        cur = Doubly(last, each, None)
        if isinstance(each, Operator):
            ops.append(cur)

        last.r = cur
        last = cur

    final = Doubly(last, None, None)
    last.r = final

    # precedence
    ops.sort(key=lambda x: precedences[x.v.opname], reverse=True)

    # associativity
    op_chunks = chunk_by(
        lambda x: (precedences[x.v.opname], associativities[x.v.opname]), ops)
    ops = []
    for ((_, is_right_asoc), chunk) in op_chunks:
        ops.extend(reversed(chunk) if is_right_asoc else chunk)

    for op in ops:
        op_v = op.v.opname
        op.v = cons(op_v)(op.l.v, op.r.v)
        op.l = op.l.l
        op.r = op.r.r
        op.l.r = op
        op.r.l = op
    return final.l.v
