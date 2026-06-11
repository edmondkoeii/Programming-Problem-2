def learn_theta(data, colors):
    max_blue = max(x for x, c in zip(data, colors) if c == 'blue')
    min_red = min(x for x, c in zip(data, colors) if c == 'red')
    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):
    loss = 0
    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    best_theta = None
    best_loss = float('inf')

    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return float(best_theta)


def minimize_ell_sorted(data, colors):
    n = len(data)

    red_le_theta = 0
    blue_gt_theta = sum(1 for c in colors if c == 'blue')

    best_loss = float('inf')
    best_theta = None

    for alpha in range(n):
        if colors[alpha] == 'red':
            red_le_theta += 1
        else:  
            blue_gt_theta -= 1

        loss = red_le_theta + blue_gt_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = data[alpha]

    return float(best_theta)
